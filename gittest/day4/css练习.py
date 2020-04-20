from bs4 import BeautifulSoup
import requests


url = "https://movie.douban.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
r = requests.get(url, headers=headers)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

element = soup.select('#billboard > div.billboard-bd > table')[0]
print(element)
for item in element.find_all('a'):
    print(item.text)