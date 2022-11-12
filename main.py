from wsgiref import headers
import requests
from bs4 import BeautifulSoup

import lxml


url = 'https://www.amazon.com/PlayStation-VR-Marvels-Iron-Bundle-4/dp/B08CD34NZH/ref=sr_1_5?crid=1SCAER9FX8BG7&keywords=playstation+vr+marvel%27s+iron+man+vr+bundle&qid=1663947473&sprefix=playstation++vr%2Caps%2C2820&sr=8-5'


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept-Language': 'en',
}


r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())
