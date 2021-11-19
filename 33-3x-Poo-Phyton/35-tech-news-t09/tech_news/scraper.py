import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        time.sleep(1)
    except requests.ReadTimeout:
        return None


# fetch_test = fetch(
#     "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
# )
# print(fetch_test)

# http://www.dannejaha.se/programming/google-and-seo/Na7d08fa2_cannonical/
# https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup
# https://devhints.io/css
# https://devhints.io/xpath
# https://developer.mozilla.org/pt-BR/docs/Web/CSS/:nth-child
# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = (selector.css(".z--font-bold *::text").get()).strip()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count.split()[0])

    comments_count = int(selector.css(".tec--btn::attr(data-count)").get())
    summary = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )
    sources_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = list(map(lambda el: el.strip(), sources_list))

    categories_list = selector.css("#js-categories .tec--badge::text").getall()
    categories = list(map(lambda el: el.strip(), categories_list))
    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return result


# req2_test = scrape_noticia(fetch_test)
# print(req2_test)

# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css("h3.tec--card__title a::attr(href)").getall()
    return result


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css(".tec--btn::attr(href)").get()
    return result


# Requisito 5
def get_tech_news(amount):
    url_search = "https://www.tecmundo.com.br/novidades"
    news_list = []
    while len(news_list) < amount:
        html_content_main = fetch(url_search)
        url_noticias_list = scrape_novidades(html_content_main)
        # print(url_noticias_list)
        for el in url_noticias_list:
            html = fetch(el)
            noticia = scrape_noticia(html)
            # print(noticia)
            news_list.append(noticia)
            # print(news_list)
            if len(news_list) == amount:
                break
        next_page = scrape_next_page_link(html_content_main)
        # print(next_page)
        url_search = next_page

    # print(news_list)
    create_news(news_list)
    return news_list
