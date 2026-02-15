import os
import asyncio
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get absolute path to index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Test Index Page
        index_path = os.path.join(current_dir, "../src/index.html")
        file_url = f"file://{index_path}"
        print(f"Opening {file_url}")
        await page.goto(file_url)
        assert "OTAKUSTAR" in (await page.title()).upper()

        # Test Navigation to AOT Page
        aot_link = await page.query_selector('a[href="aot.html"]')
        assert aot_link is not None
        print("AOT link found on index page.")

        # Test AOT Page
        aot_path = os.path.join(current_dir, "../src/aot.html")
        file_url = f"file://{aot_path}"
        print(f"Opening {file_url}")
        await page.goto(file_url)

        # 1. Check Title
        title = await page.title()
        print(f"AOT Page Title: {title}")
        assert "ATTACK ON TITAN" in title.upper()

        # 2. Check Logo
        logo = await page.query_selector('.logo')
        assert logo is not None
        print("Logo found on AOT page.")

        # 3. Check for Seasons Grid
        seasons = await page.query_selector_all('.season-card')
        print(f"Found {len(seasons)} season cards.")
        assert len(seasons) >= 4

        # 4. Check for Resolution Buttons
        res_btns = await page.query_selector_all('.res-btn')
        print(f"Found {len(res_btns)} resolution buttons.")
        assert len(res_btns) >= 12 # 4 seasons * 3 buttons

        # 5. Visual Check - Take Screenshot
        screenshot_path = os.path.join(current_dir, "aot_page_test.png")
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"AOT page screenshot saved to {screenshot_path}")

        print("\n✅ All AOT integration tests passed!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_tests())
