from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup

html = requests.get("https://habr.com/ru/all");
parsered_html = BeautifulSoup(html.text, "html.parser")

title_links = parsered_html.select(".tm-article-snippet__title-link")

for span in title_links:
    print(Fore.RED + span.contents[0].contents[0] + Fore.GREEN +" (" + span["href"] + ")")

# Нужно что бы терминал был нормального цвета
print(Fore.WHITE) 
