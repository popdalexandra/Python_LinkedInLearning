# o modalitate de a creea un API pentru un site web care nu are un API
# folosim pagina pixelford.com ca exemplu pe care lucram

import requests
from bs4 import BeautifulSoup
import datetime

# verificam cum arata datele pe site ul web
url = "https://pixelford.com/blog/"
response = requests.get(url, headers = {'user-agent': 'Hello'}) # am pus headers pentru a nu da eroare
html = response.content
# print(response.content) # text HTML
# print(requests.utils.default_headers)

soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="type-post")
# a_tags = soup.find_all('a', class_="entry-title-link")  # afiseaza toate tagurile <a> din clasele egale cu ...


# for a_tag in a_tags:
#     print(a_tag.get_text()) # afiseaza toate titlurile

# titles = list(map(lambda a_tag: a_tag.get_text(),a_tags))
# print(titles)

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
    time_string = blog.find('time', class_="entry-time").get('datetime')
    time = datetime.datetime.fromisoformat(time_string) # formatarea zilei, lunii, anului : vezi : strftime.org
    time_format = time.strftime("%b %d %Y ")

    print(f"{time_format} - {title}")