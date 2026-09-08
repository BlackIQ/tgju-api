import httpx
from bs4 import BeautifulSoup

from schemas.price import PriceItem, PriceCategory

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

CURRENCY_URL = "https://www.tgju.org/currency"
GOLD_URL = "https://www.tgju.org/gold-chart"
OIL_URL = "https://www.tgju.org/energy"


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


def parse_price_row(row) -> PriceItem:
    title = row.find("th").get_text(strip=True)
    price = row.find("td", class_="nf").get_text(strip=True)

    low_price, high_price = get_price_range(row)

    link = row.select_one("td.chart-td a")

    if not link or not link.get("href"):
        raise ValueError(f"Price row has no profile link: {title}")

    key = link["href"].rstrip("/").split("/")[-1]

    return PriceItem(
        title=title,
        price=price,
        key=key,
        status=get_price_status(row),
        low_price=low_price,
        high_price=high_price,
    )


def get_price_rows(table):
    return table.select("tbody > tr:not(.market-cat-title-tr)")


async def get_currency_prices() -> list[PriceItem]:
    soup = await _get_soup(CURRENCY_URL)

    return [
        parse_price_row(row)
        for table in soup.select("table.market-table")
        for row in get_price_rows(table)
    ]


async def get_gold_prices() -> list[PriceCategory]:
    soup = await _get_soup(GOLD_URL)

    categories: list[PriceCategory] = []

    for table in soup.select("table.market-table"):
        category_title = table.find("th").get_text(strip=True)

        prices = [parse_price_row(row) for row in get_price_rows(table)]

        categories.append(
            PriceCategory(
                title=category_title,
                prices=prices,
            )
        )

    return categories


async def get_oil_prices() -> list[PriceCategory]:
    soup = await _get_soup(OIL_URL)

    categories: list[PriceCategory] = []

    for table in soup.select("table.market-table"):
        category_title = table.find("th").get_text(strip=True)

        prices = [parse_price_row(row) for row in get_price_rows(table)]

        categories.append(
            PriceCategory(
                title=category_title,
                prices=prices,
            )
        )

    return categories
