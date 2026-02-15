
import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Monitor console logs
        page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}"))

        path = os.path.abspath("src/index.html")
        await page.goto(f"file://{path}")

        # Wait for page to load
        await page.wait_for_load_state("networkidle")

        # Scroll down to bottom slowly to trigger all observers
        await page.evaluate("""
            async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    let distance = 100;
                    let timer = setInterval(() => {
                        let scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;
                        if(totalHeight >= scrollHeight){
                            clearInterval(timer);
                            resolve();
                        }
                    }, 50);
                });
            }
        """)

        # Wait more for animations to complete
        await asyncio.sleep(3)

        # Check elements
        # Note: script.js sets opacity 0 and observer sets it back to 1 via anime.js
        # We check computed opacity
        stats = await page.evaluate("""
            () => {
                const getOpacity = (el) => window.getComputedStyle(el).opacity;
                const chars = Array.from(document.querySelectorAll('.char-card'));
                const news = Array.from(document.querySelectorAll('.news-item'));
                const titles = Array.from(document.querySelectorAll('.section-title'));

                return {
                    charCount: chars.length,
                    newsCount: news.length,
                    titleCount: titles.length,
                    visibleChars: chars.filter(el => parseFloat(getOpacity(el)) > 0).length,
                    visibleNews: news.filter(el => parseFloat(getOpacity(el)) > 0).length,
                    visibleTitles: titles.filter(el => parseFloat(getOpacity(el)) > 0).length
                };
            }
        """)
        print(f"Stats: {stats}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
