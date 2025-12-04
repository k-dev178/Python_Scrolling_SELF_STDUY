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
