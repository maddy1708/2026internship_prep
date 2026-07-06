import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.find_all("div", class_="card-content")

jobs = []

for job in job_cards:
    title = job.find("h2").text.strip()
    company = job.find("h3").text.strip()
    location = job.find("p", class_="location").text.strip()

    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location
    })

df = pd.DataFrame(jobs)

print(df.head())

df.to_csv("jobs.csv", index=False)

print("Data saved successfully!")