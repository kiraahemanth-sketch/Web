from playwright.sync_api import sync_playwright

def verify_premium_look():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto(f'file:///app/src/index.html')

        # Wait for animations
        page.wait_for_timeout(2000)

        # Capture Hero
        page.screenshot(path='tests/premium_hero.png')

        # Scroll to characters
        page.evaluate("window.scrollTo(0, 1000)")
        page.wait_for_timeout(1000)
        page.screenshot(path='tests/premium_characters.png')

        # Scroll to news
        page.evaluate("window.scrollTo(0, 2000)")
        page.wait_for_timeout(1000)
        page.screenshot(path='tests/premium_news.png')

        browser.close()

if __name__ == "__main__":
    verify_premium_look()
