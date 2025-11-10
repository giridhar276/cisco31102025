### requests library is used to read html/xml content from http page
# step1:  connect to url and get the html content  ( requests)
# step2:  read html content and display all the urls ( beautifulsoup)

from bs4 import BeautifulSoup
import requests 
url = "https://www.google.com/"

try:
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            if url.startswith("http"):
                print(url)
                print("-------------")
            
except Exception as err:
    print(err)


