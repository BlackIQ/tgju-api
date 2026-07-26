# FastAPI
from fastapi import APIRouter

# Schemas
from schemas.price import CurrencyCategory, GoldCategory

# Scrapper
from scrap.tgju import get_currency_prices, get_gold_prices

# Router
router = APIRouter(
    prefix="/price",
    tags=["Price"],
)


@router.get("/currency", response_model=list[CurrencyCategory])
async def currency():
    """
    ### Example:

    Here I put an example for you.

    ```json
    [
        {
            "title": "دلار",
            "price": "1,872,000",
            "key": "price_dollar_rl",
            "status": "low",
            "low_price": "1,868,800",
            "high_price": "1,892,000"
        },
        {
            "title": "یورو",
            "price": "2,133,000",
            "key": "price_eur",
            "status": "low",
            "low_price": "2,129,600",
            "high_price": "2,156,300"
        },
        {
            "title": "درهم امارات",
            "price": "511,680",
            "key": "price_aed",
            "status": "low",
            "low_price": "510,860",
            "high_price": "520,240"
        },
        {
            "title": "دینار کویت",
            "price": "6,051,300",
            "key": "price_kwd",
            "status": "low",
            "low_price": "6,024,800",
            "high_price": "6,097,600"
        },
        {
            "title": "روبل روسیه",
            "price": "23,960",
            "key": "price_rub",
            "status": "low",
            "low_price": "23,920",
            "high_price": "24,220"
        }
    ]
    ```
    """

    return await get_currency_prices()


@router.get("/gold", response_model=list[GoldCategory])
async def gold():
    """
    ### Example:

    Here I put an example for you.

    ```json
    [
        {
            "title": "قیمت طلا",
            "prices": [
                {
                    "title": "طلای 18 عیار / 750",
                    "price": "180,523,000",
                    "key": "geram18",
                    "status": "low",
                    "low_price": "178,690,000",
                    "high_price": "182,568,000"
                },
                {
                    "title": "طلای 18 عیار / 740",
                    "price": "178,116,000",
                    "key": "gold_740k",
                    "status": "low",
                    "low_price": "176,308,000",
                    "high_price": "180,134,000"
                },
                {
                    "title": "طلای ۲۴ عیار",
                    "price": "240,695,000",
                    "key": "geram24",
                    "status": "low",
                    "low_price": "238,251,000",
                    "high_price": "243,422,000"
                },
                {
                    "title": "طلای دست دوم",
                    "price": "178,116,050",
                    "key": "gold_mini_size",
                    "status": "low",
                    "low_price": "176,307,540",
                    "high_price": "180,134,120"
                }
            ]
        }
    ]
    ```
    """

    return await get_gold_prices()
