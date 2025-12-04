# 스크롤할 웹사이트
- https://weworkremotely.com
- https://remoteok.com
- https://www.wanted.co.kr

---

# 패키지 설치
beautifulsoup4, requests

---

# 1. 정적 페이지 크롤링

## 1.1 BeautifulSoup
HTML을 파싱(분석)해서 원하는 데이터를 추출하는 라이브러리.

## 1.2. 사용법
```py
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, "html.parser")
```
response.content는 requests로 받아온 HTML 내용임.
"html.parser"는 HTML을 분석하겠다는 뜻.

## 1.3. find, find_all
find는 html 요소 하나를 반환.
find_all은 요소들을 리스트로 반환.

그래서 find는 id또는 class가 하나만 있거나, 하나만 크롤링 하고싶을때 사용.
find_all는 class를 모두 긁어 오고 싶을때 사용.

* class 크롤링
```py
title = soup.find_all(class_="bjs-jlid__h")

title = soup.find_all("div", class_="bjs-jlid__h") # div를 붙여서 크롤링 범위를 더 줄일 수 있음.
```
* id 크롤링
```py
title = soup.find_all(id="btn")

title = soup.find_all("div", id="btn") # div를 붙여서 크롤링 범위를 더 줄일 수 있음.
```

## 1.4. 페이지가 나뉘어있는 경우
보통 get방식 페이지들은, url에 페이지 번호를 나타냄.

> 예시)
> 
> https://weworkremotely.com/remote-full-time-jobs?page=2

저걸 가지고 크롤링 가능.

```py
all_jobs = []

def scrape_url(url):
    print(f"scraping {url}...")
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find_all(class_="title")
    company = soup.find_all(class_="company")
    description = soup.find_all(class_="description")

    data = {
        "title" : title,
        "company" : company,
        "description" : description
    }

    all_jobs.append(data)
    

res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")

buttons = len(soup.find_all(class_="page-numbers")) - 1

for i in range(buttons):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
    scrape_url(url)

print(f"jobs: {len(all_jobs)}")
```

# 2. 동적 페이지 크롤링

## 기본구조
```py
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=True) # False: 브라우저 보기, True : 브라우저 안보기

page = browser.new_page()
page.goto("https://google.com")

page.screenshot(path="a.png")
```

## 클릭
```html
<button id="btn"></button>
<div class="btns"></div>
```
```py
page.click("button#btn")
page.click("div.btns")
```

## 글자 채우기
```py
page.get_by_placeholder("flutter")
```

## 키보드 누르기
```py
page.keyboard.down("End")
```

## 페이지 반환
```py
content = page.content()

soup = BeautifulSoup(content, "html.parser")
```