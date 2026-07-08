from bs4 import BeautifulSoup

def extract_jobs(html):

    soup = BeautifulSoup(html, "html.parser")

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

    return jobs