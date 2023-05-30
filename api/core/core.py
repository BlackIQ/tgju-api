import requests
from bs4 import BeautifulSoup


def gold():
    url = "https://www.tgju.org/gold-chart"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    tables = soup.find_all('table', class_='market-table')

    out = []

    for table in tables:
        body = table.find('tbody')
        rows = body.find_all('tr')

        title = table.find('th').text

        prices = []

        for item in rows:
            item_title = item.find('th').text
            item_price = item.find('td', class_='nf').text

            prices.append({'title': item_title, 'price': item_price})

        out.append({'title': title, 'prices': prices})

    return out
