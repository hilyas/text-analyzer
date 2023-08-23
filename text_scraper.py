import requests
from bs4 import BeautifulSoup
from typing import Optional


class WebRequester:
    def __init__(self, user_agent: Optional[str] = None):
        default_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        self.headers = {
            "User-Agent": user_agent if user_agent else default_agent
        }

    def fetch_content(self, url: str) -> str:
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.content
        except requests.RequestException as e:
            print(f"An error occurred while fetching the URL: {e}")
            return ""


class TextScraper:
    def __init__(self, requester: WebRequester):
        self.requester = requester
        self.soup = None

    def scrape_website(self, url: str) -> str:
        html_content = self.requester.fetch_content(url)
        if not html_content:
            return ""

        self.soup = BeautifulSoup(html_content, "html.parser")
        paragraphs = self.soup.find_all("p")
        content = " ".join([para.get_text() for para in paragraphs])
        return content
