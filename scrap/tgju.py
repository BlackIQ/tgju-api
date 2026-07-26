# HTTPX
import httpx

# Beautiful soap v4
from bs4 import BeautifulSoup

# Schemas
from schemas.price import PriceItem, GoldCategory

# Sample header
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


# Get soup function
async def _get_soup(url: str) -> BeautifulSoup:
    async with httpx.AsyncClient(
        headers=HEADERS,
        follow_redirects=True,
        timeout=20,
    ) as client:
        response = await client.get(url)
        response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


# Currency scrapper
async def get_currency_prices() -> list[PriceItem]:
    soup = await _get_soup("https://www.tgju.org/currency")

    output: list[PriceItem] = []

    for table in soup.select("table.market-table"):
        for row in table.select("tbody > tr"):

            title = row.find("th").get_text(strip=True)

            price = row.find("td", class_="nf").get_text(strip=True)

            href = row.find_all("td")[-1].a["href"]

            output.append(
                PriceItem(
                    title=title,
                    price=price,
                    key=href.split("/")[-1],
                )
            )

    return output


# Gold scrapper
async def get_gold_prices() -> list[GoldCategory]:
    soup = await _get_soup("https://www.tgju.org/gold-chart")

    categories: list[GoldCategory] = []

    for table in soup.select("table.market-table"):

        category_title = table.find("th").get_text(strip=True)

        prices: list[PriceItem] = []

        for row in table.select("tbody > tr"):

            title = row.find("th").get_text(strip=True)

            price = row.find("td", class_="nf").get_text(strip=True)

            href = row.find_all("td")[-1].a["href"]

            prices.append(
                PriceItem(
                    title=title,
                    price=price,
                    key=href.split("/")[-1],
                )
            )

        categories.append(
            GoldCategory(
                title=category_title,
                prices=prices,
            )
        )

    return categories
