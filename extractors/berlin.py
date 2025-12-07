import requests
from bs4 import BeautifulSoup


def extract_indeed_jobs(keyword):
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    
    response = requests.get(   
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    jobs = []
    
    title = soup.find_all(class_="bjs-jlid__h")
    company = soup.find_all(class_="bjs-jlid__b")
    description = soup.find_all(class_="bjs-jlid__description")

    for i in range(len(title)):
        a_tag = title[i].find("a")
        href = a_tag.get("href") if a_tag else None
        
        job = {
            "title": title[i].text.strip(),
            "company": company[i].text.strip() if i < len(company) else "None",
            "description": description[i].text.strip() if i < len(description) else "None",
            "link": href if href else "None"
        }
        jobs.append(job)

    return jobs