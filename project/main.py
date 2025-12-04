from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # False: 브라우저 보기, True : 브라우저 안보기

page = browser.new_page()
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

for i in range(3):
    page.keyboard.down("End")
    time.sleep(2)

content = page.content()

p.stop()

# beautifulsoup
soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div",class_="JobCard_container__zQcZs")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong",class_="JobCard_title___kfvj").text
    company_name = job.find("span",class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu").text
    reward = job.find("span",class_="JobCard_reward__oCSIQ").text

    job = {
        "link" : link,
        "title" : title,
        "company_name" : company_name,
        "reward" : reward
    }

    jobs_db.append(job)

file = open("./project/ToExcel.py/jobs.csv", 'w' ,encoding="utf-8")
w = csv.writer(file) # w = writer
w.writerow(["link", "title", "company", "reward"])

for job in jobs_db:
    w.writerow(job.values())
