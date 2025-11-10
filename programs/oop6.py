


import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page_content = None

    def fetch_content(self):
        """Fetch the HTML content of the URL"""
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.page_content = response.text
                print(f"Successfully fetched content from: {self.url}")
            else:
                print(f"Failed to fetch page. Status Code: {response.status_code} - {self.url}")
        except Exception as e:
            print(f"Error fetching the page: {e} - {self.url}")

    def show_title(self):
        """Parse the HTML and print the title of the page"""
        if self.page_content:
            soup = BeautifulSoup(self.page_content, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            print(f"Page Title: {title}")
        else:
            print("No page content available. Please fetch content first.")

    def show_links(self):
        """Extract and print all hyperlinks from the page"""
        if self.page_content:
            soup = BeautifulSoup(self.page_content, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                print(link['href'])
            else:
                print("No links found on the page.")
        else:
            print("No page content available. Please fetch content first.")


if __name__ == "__main__":  
    urls = [
            "https://www.wikipedia.org",
            "https://www.python.org"
        ]

    for url in urls:
        print(f"\n📄 Scraping URL: {url}")
        scraper = WebScraper(url)
        scraper.fetch_content()
        scraper.show_title()
        scraper.show_links()