# flask 설치방법
## 기본 설치
```bash
pip install flask
```

## 가상환경에서 설치
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# Flask 설치
pip install flask
```

## 실행
```bash
.venv/bin/python3 main.py
```

---

# flask 기본적인 코드
## 코드
```py
from flask import Flask

app = Flask("main")

@app.route("/")
def main():
    return "<h1>Hello World</h1>"

app.run("0.0.0.0", port=8080)
```
## 설명
"0.0.0.0"이 기본. port는 8080추천.

@app.route("/")에서 "/"은 경로를 말함.<br>
그 바로 아래에 함수에서 리턴을 시키면 html 형태로 페이지를 간단하게 만들어줌.

---

# render_template
"<h1>Hello World</h1>" 대신 복잡한 html 코드를 반환시킬 수도 있음.

## 코드
```py
from flask import render_template

@app.route("/hello")
def main():
    return render_template("hello.html", name="ksj")
```

```html
/* templates/hello.html */
<body>
    <h1>Hello</h1>
    <h4>My name is {{name}}</h4>
</body>
```
## 설명
html 경로 뒤에 name = "ksj"처럼 변수를 만들어서 html에게 전달 가능.

---

# from action
## 코드
```html
/* templates/home.html */

<body>
    <h1>Job Scrapper</h1>
    <h4>What job do you want?</h4>
    <form action="/search">
        <input type="text" name="keyword" placeholder="Write one keyword please" />
        <button>Search</button>
    </form>
</body>
```

```py
@app.route("/search")
def search():
    return render_template("search.html")
```

```html
/* templates/search.html */

<body>
    <h1>Search Results</h1>
</body>
```
1. 버튼을 누르면 액션.
2. 플래스크.py로 이동. 
3. "/search" 찾은 후, render_template에 의해 "search.html"로 이동.
