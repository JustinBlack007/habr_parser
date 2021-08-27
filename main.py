from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup


search_query = input("Введите запрос: ")

def search_posts(text_of_query):
    payload = {"q": search_query, "target_type": "posts", "order": "relevance"}
    html = requests.get("https://habr.com/ru/search/", params=payload);
    parsered_html = BeautifulSoup(html.text, "html.parser")


    all_posts = parsered_html.select(".tm-article-snippet__title-link")

    for post in all_posts:
        title_of_post = ""
        link_of_post = "https://habr.com" + post["href"]
        for text in post.contents[0].strings:
            title_of_post += text
        
        title_of_post = Fore.RED + title_of_post
        link_of_post = Back.RESET + Fore.GREEN + link_of_post
        
        print(f"{title_of_post} \n ({link_of_post}) \n")



# Нужно что бы терминал был нормального цвета
search_posts(search_query)
print(Style.RESET_ALL)
