import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Get the absolute path to index.html
        path = os.path.abspath("src/index.html")
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        await page.goto(f"file://{path}")

        # Wait for anime.js to start
        await page.wait_for_timeout(2000)

        # Scroll down to trigger reveal animations
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
                    }, 100);
                });
            }
        """)

        # Wait for animations to finish
        await page.wait_for_timeout(2000)

        # Take a better full page screenshot
        await page.screenshot(path="full_page_scrolled.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
