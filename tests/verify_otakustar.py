import os
import asyncio
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get absolute path to index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, "../src/index.html")
        file_url = f"file://{html_path}"

        print(f"Opening {file_url}")
        await page.goto(file_url)

        # 1. Check Title
        title = await page.title()
        print(f"Page Title: {title}")
        assert "OTAKUSTAR" in title.upper()

        # 2. Check Logo
        logo = await page.query_selector('.logo')
        logo_text = await logo.inner_text()
        print(f"Logo Text: {logo_text}")
        assert "OTAKUSTAR" in logo_text.upper()

        # 3. Check for Sakura Container
        sakura = await page.query_selector('#sakura-container')
        assert sakura is not None
        print("Sakura container found.")

        # 4. Check for reCAPTCHA script
        recaptcha_script = await page.query_selector('script[src*="recaptcha/api.js"]')
        assert recaptcha_script is not None
        print("reCAPTCHA script found.")

        # 5. Check for Watermark
        watermark = await page.query_selector('.watermark-overlay')
        assert watermark is not None
        print("Background watermark found.")

        # 6. Check for Footer Watermark
        footer_watermark = await page.query_selector('.footer-watermark')
        assert footer_watermark is not None
        print("Footer watermark found.")

        print("\n✅ All tests passed!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_tests())
