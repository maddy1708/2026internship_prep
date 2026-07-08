import requests

def fetch_html(url):
    response = requests.get(url)
    return response.text