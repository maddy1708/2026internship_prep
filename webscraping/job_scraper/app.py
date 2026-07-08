from scraper.fetch import fetch_html
from scraper.parser import extract_jobs
from scraper.exporter import save_csv

url = "https://realpython.github.io/fake-jobs/"

html = fetch_html(url)

jobs = extract_jobs(html)

save_csv(jobs)

print("Done!")