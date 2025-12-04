from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=True) # False: 브라우저 보기, True : 브라우저 안보기

page = browser.new_page()
page.goto("https://google.com")

page.screenshot(path="a.png")