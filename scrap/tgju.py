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


def get_price_status(row) -> str | None:
    status = row.select_one("td.nf span")

    if not status:
        return None

    classes = status.get("class", [])

    for item in classes:
        if item in ["low", "high"]:
            return item

    return None


def get_price_range(row) -> tuple[str | None, str | None]:
    cells = row.find_all("td")

    if len(cells) < 4:
        return None, None

    low_price = cells[2].get_text(strip=True)
    high_price = cells[3].get_text(strip=True)

    return low_price, high_price


# Currency scrapper
async def get_currency_prices() -> list[PriceItem]:
    soup = await _get_soup("https://www.tgju.org/currency")

    output: list[PriceItem] = []

    for table in soup.select("table.market-table"):
        for row in table.select("tbody > tr"):
            title = row.find("th").get_text(strip=True)

            price = row.find("td", class_="nf").get_text(strip=True)
            low_price, high_price = get_price_range(row)

            href = row.find_all("td")[-1].a["href"]

            output.append(
                PriceItem(
                    title=title,
                    price=price,
                    key=href.split("/")[-1],
                    status=get_price_status(row),
                    low_price=low_price,
                    high_price=high_price,
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
            low_price, high_price = get_price_range(row)

            href = row.find_all("td")[-1].a["href"]

            prices.append(
                PriceItem(
                    title=title,
                    price=price,
                    key=href.split("/")[-1],
                    status=get_price_status(row),
                    low_price=low_price,
                    high_price=high_price,
                )
            )

        categories.append(
            GoldCategory(
                title=category_title,
                prices=prices,
            )
        )

    return categories
