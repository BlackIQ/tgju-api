import requests
from bs4 import BeautifulSoup


def gold():
    gold_url = "https://www.tgju.org/gold-chart"

    g_r = requests.get(gold_url)

    g_soup = BeautifulSoup(g_r.content, 'html.parser')

    g_tables = g_soup.find_all('table', class_='market-table')

    g_out = []

    for table in g_tables:
        body = table.find('tbody')
        rows = body.find_all('tr')

        title = table.find('th').text

        prices = []

        for item in rows:
            item_title = item.find('th').text
            item_price = item.find('td', class_='nf').text
            item_key = item.find_all(
                'td')[-1].find('a').get('href').split('/')[-1]

            prices.append(
                {'title': item_title, 'price': item_price, 'key': item_key})

        g_out.append({'title': title, 'prices': prices})

    return g_out


def currency():
    currency_url = "https://www.tgju.org/currency"

    c_r = requests.get(currency_url)

    c_soup = BeautifulSoup(c_r.content, 'html.parser')

    c_tables = c_soup.find_all('table', class_='market-table')

    c_out = []

    for table in c_tables:
        body = table.find('tbody')
        rows = body.find_all('tr')

        for row in rows:
            title = row.find('th').text
            price = row.find('td', class_='nf').text
            key = row.find_all('td')[-1].find('a').get('href').split('/')[-1]

            c_out.append({'title': title, 'price': price, 'key': key})

    return c_out
