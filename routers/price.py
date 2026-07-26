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
        { "title": "دلار", "price": "1,868,850", "key": "price_dollar_rl" },
        { "title": "یورو", "price": "2,129,800", "key": "price_eur" },
        { "title": "درهم امارات", "price": "510,900", "key": "price_aed" },
        { "title": "پوند انگلیس", "price": "2,488,600", "key": "price_gbp" },
        { "title": "لیر ترکیه", "price": "39,500", "key": "price_try" },
        { "title": "یوان چین", "price": "275,900", "key": "price_cny" },
        { "title": "روبل روسیه", "price": "23,920", "key": "price_rub" }
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
                    "price": "180,421,000",
                    "key": "geram18"
                },
                {
                    "title": "طلای 18 عیار / 740",
                    "price": "178,016,000",
                    "key": "gold_740k"
                },
                {
                    "title": "طلای ۲۴ عیار",
                    "price": "240,560,000",
                    "key": "geram24"
                },
                {
                    "title": "طلای دست دوم",
                    "price": "178,015,830",
                    "key": "gold_mini_size"
                }
            ]
        },
        {}
    ]
    ```
    """

    return await get_gold_prices()
