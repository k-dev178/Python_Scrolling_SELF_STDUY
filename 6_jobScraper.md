# 스크롤할 웹사이트
- https://weworkremotely.com
- https://remoteok.com
- https://www.wanted.co.kr

---

# 패키지 설치
beautifulsoup4, requests

---

# 1. BeautifulSoup
HTML을 파싱(분석)해서 원하는 데이터를 추출하는 라이브러리.

## 1.1. 사용법
```py
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, "html.parser")
```
response.content는 requests로 받아온 HTML 내용임.
"html.parser"는 HTML을 분석하겠다는 뜻.

---

# 2. find & find_all
HTML에서 원하는 요소를 찾는 메소드.

## 2.1. find
조건에 맞는 첫 번째 요소만 찾음.
```py
soup.find(class_="header")

#출력
<div class="header">...</div>
```
못 찾으면 None을 반환함.

## 2.2. find_all
조건에 맞는 모든 요소를 찾음.
```py
soup.find_all(class_="page")

#출력
[<span class="page">1</span>, <span class="page">2</span>, ...]
```
리스트로 반환함.

## 2.3. class_를 쓰는 이유
파이썬에서 class는 예약어라서 class_ 라고 써야함.
```py
soup.find(class_="listing")  # O
soup.find(class="listing")   # X 에러남
```

## 2.4. 다양한 찾기 방법
```py
# 태그로 찾기
soup.find("div")
soup.find_all("a")

# 태그 + 클래스 조합
soup.find("div", class_="header")

# id로 찾기
soup.find(id="main-content")
```

---

# 3. 요소에서 데이터 추출

## 3.1. text
요소 안의 텍스트를 가져옴.
```py
title = job.find(class_="title").text

#출력
"  Frontend Developer  "
```

## 3.2. strip()
앞뒤 공백을 제거함.
```py
title = job.find(class_="title").text.strip()

#출력
"Frontend Developer"
```

## 3.3. 속성값 가져오기
```py
link = element["href"]
img_src = element["src"]
```

---

# 4. None 체크
요소가 없을 수도 있으니까 체크해야함.
```py
region_tag = job.find(class_="headquarters")

if region_tag:
    region = region_tag.text.strip()
    if not region:
        region = "None"
else:
    region = "None"
```
find()가 못 찾으면 None을 반환하는데, None.text 하면 에러남.
그래서 if로 먼저 체크해야함.

---

# 5. 페이지네이션
여러 페이지를 순회하면서 데이터를 수집하는 방법.

## 5.1. 페이지 수 파악
```py
buttons = len(soup.find(class_="pagination").find_all(class_="page"))
```
pagination 안에 있는 page 클래스 개수를 세서 총 페이지 수를 알아냄.

## 5.2. 각 페이지 순회
```py
for i in range(buttons):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
    scrape_url(url)
```
range(buttons)로 반복하면서 각 페이지 URL을 만들어서 스크래핑함.

---

# 6. 데이터 구조화
스크래핑한 데이터를 딕셔너리로 정리해서 리스트에 저장.
```py
all_jobs = []

job_data = {
    "title": title,
    "company": company,
    "position": position,
    "region": region
}

all_jobs.append(job_data)
```
나중에 all_jobs를 출력하면 모든 채용공고 정보가 담긴 리스트가 나옴.

---

# 7. 전체 흐름
```
1. requests.get()으로 웹페이지 요청
2. BeautifulSoup으로 HTML 파싱
3. find_all()로 원하는 요소들 찾기
4. 각 요소에서 필요한 데이터 추출
5. 딕셔너리로 정리해서 리스트에 저장
6. 페이지네이션으로 다음 페이지 반복
```
