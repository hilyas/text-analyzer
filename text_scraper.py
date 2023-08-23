import requests
from bs4 import BeautifulSoup

class TextScraper:
    def __init__(self):
        self.soup = None

    def scrape_website(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = self.soup.find_all("p")
        content = " ".join([para.get_text() for para in paragraphs])
        return content