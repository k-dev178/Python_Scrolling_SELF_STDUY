from playwright.sync_api import sync_playwright
import time

pw = "Java123%%na"
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()
page.goto("https://naver.com")
time.sleep(1)

page.click("a.MyView-module__link_login___HpHMW")
time.sleep(1)

# id
page.get_by_label("아이디 또는 전화번호").fill("gwisej68")
time.sleep(1)

# pw
page.get_by_label("비밀번호").fill(f"{pw}")
time.sleep(1)

page.keyboard.down("Enter")
time.sleep(1)

page.click("a.btn")
time.sleep(10)

page.close()