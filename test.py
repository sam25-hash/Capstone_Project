from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True to hide browser
        page = browser.new_page()
        page.goto("https://practicesoftwaretesting.com/")
        time.sleep(2)  # wait for page to load

        # ------------------------
        # Scroll gradually from top to bottom
        # ------------------------
        height = page.evaluate("() => document.body.scrollHeight")
        step = 300
        for i in range(0, height, step):
            page.evaluate(f"window.scrollTo(0, {i})")
            time.sleep(0.3)

        # Scroll back to top
        for i in range(height, -1, -step):
            page.evaluate(f"window.scrollTo(0, {i})")
            time.sleep(0.3)

        # ------------------------
        # Hover over all <a> links
        # ------------------------
        links = page.query_selector_all("a")
        for link in links:
            try:
                link.hover()
                text = link.inner_text()
                print(f"Hovered over link: {text}")
                time.sleep(0.1)
            except:
                continue

        # ------------------------
        # Print full page HTML in console
        # ------------------------
        html_content = page.content()
        print(html_content)  # prints entire HTML to console

        browser.close()

if __name__ == "__main__":
    run()
