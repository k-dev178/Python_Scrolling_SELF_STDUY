from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class scrape_wanted:
    def __init__(self,position,num):
        url = f"https://www.wanted.co.kr/search?query={position}&tab=position"

        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False) # False: 브라우저 보기, True : 브라우저 안보기

        page = browser.new_page()

        page.goto(url)

        for i in range(num):
            page.keyboard.down("End")
            time.sleep(2)

        self.content = page.content()

        p.stop()
    
    def soup(self):
        content = self.content
        soup = BeautifulSoup(content, "html.parser")

        jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

        self.jobs_db = []
        for job in jobs:
            title = job.find("strong", class_="JobCard_title___kfvj").text
            company = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu").text
            requirement = job.find("span", class_= "CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l").text
            reward = job.find("span", class_="JobCard_reward__oCSIQ").text

            data = {
                "title" : title,
                "company" : company,
                "requirement" : requirement,
                "reward" : reward
            }

            self.jobs_db.append(data)

    def jobs_len(self):
        jobs_db = self.jobs_db
        return len(jobs_db)
    
    def write_csv(self, url):
        jobs_db = self.jobs_db

        file = open(url, 'w' ,encoding="utf-8")
        w = csv.writer(file) # w = writer
        w.writerow(["link", "title", "company", "reward"])

        for job in jobs_db:
            w.writerow(job.values())

flutter = scrape_wanted("flutter", 3)
flutter.soup()

nextjs = scrape_wanted("nextjs", 8)
nextjs.soup()

kotlin = scrape_wanted("kotlin", 9)
kotlin.soup()

print(f"flutter: {flutter.jobs_len()}")
flutter.write_csv("./project/ToExcel.py/flutter.csv")

print(f"nextjs: {nextjs.jobs_len()}")
nextjs.write_csv("./project/ToExcel.py/nextjs.csv")

print(f"kotlin: {kotlin.jobs_len()}")
kotlin.write_csv("./project/ToExcel.py/kotlin.csv")