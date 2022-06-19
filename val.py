from bs4 import BeautifulSoup
import requests
import random
response = requests.get('https://bank.gov.ua')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'<div class="value">'})
    res = soup_list[0].find('<div class="value">')
    print(res.text)
b = res
a = random.randint(100, 200)
print(a, " гривень це", a/b, "доларів США")