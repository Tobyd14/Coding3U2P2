import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.co.uk/Apple-iPhone-64-GB-Space/dp/B075V3RKP3/ref=sr_1_1_sspa?keywords=iphone+8&qid=1581307728&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQzJOTllaODVGNThDJmVuY3J5cHRlZElkPUEwNzIzODA0M0tNT1ZVUUJXOE5JTiZlbmNyeXB0ZWRBZElkPUEwMTM3OTcyMUNBWk02Rko2T0RaNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User_Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')