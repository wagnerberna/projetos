import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # pass
    noticias = db.find_news()
    find_result = []

    for el in noticias:
        if el["title"].lower() == title.lower():
            find_result.append((el["title"], el["url"]))

    return find_result


# test_req06 = search_by_title("Musk")

# print(test_req06)

# https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
def date_check(date):
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    # pass
    date_check(date)
    noticias = db.find_news()
    find_result = []
    for el in noticias:
        if (el["timestamp"]).startswith(date):
            find_result.append((el["title"], el["url"]))

    return find_result


# Requisito 8
def search_by_source(source):
    # pass
    noticias = db.find_news()
    find_result = []

    for noticia in noticias:
        # print(noticia)
        # print(noticia["sources"])
        for el in noticia["sources"]:
            # print("----")
            # print(el)
            if el.lower() == source.lower():
                find_result.append((noticia["title"], noticia["url"]))

    return find_result


# Requisito 9
def search_by_category(category):
    # pass
    noticias = db.find_news()
    find_result = []

    for noticia in noticias:
        for el in noticia["categories"]:
            if el.lower() == category.lower():
                find_result.append((noticia["title"], noticia["url"]))

    return find_result
