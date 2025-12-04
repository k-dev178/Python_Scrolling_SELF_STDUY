from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # False: 브라우저 보기, True : 브라우저 안보기

page = browser.new_page()
page.goto("https://www.wanted.co.kr")
time.sleep(1)

# 페이지 조작
page.click("button.Aside_searchButton__Ib5Dn")
time.sleep(1)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(1)

page.keyboard.down("Enter")
time.sleep(1)

page.click("a#search_tab_position")
time.sleep(1)

for i in range(5):
    page.keyboard.down("End")
    time.sleep(2)

content = page.content()

p.stop()

# beautifulsoup
soup = BeautifulSoup(content, "html.parser")