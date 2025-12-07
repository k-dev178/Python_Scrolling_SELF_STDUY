from flask import Flask, render_template, request
from extractors.berlin import extract_indeed_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="ksj")

@app.route("/hello")
def hello():
    return "hello you!"

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword in db:
        berlin = db[keyword]
    else:
        berlin = extract_indeed_jobs(keyword)
        db[keyword] = berlin

    return render_template("search.html",keyword=keyword, jobs = berlin)

app.run("0.0.0.0", port=8080)