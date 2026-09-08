# Libs
import json  # JSON

# Application
from core.redis_sync import redis  # Core: Redis
from scrap.tgju import (
    get_currency_prices,
    get_gold_prices,
    get_oil_prices,
)  # Scrapper: TGJU


async def currency():
    data = await get_currency_prices()

    prices = json.dumps(
        [item.model_dump() for item in data],
        ensure_ascii=False,
    )

    redis.set("tgju:currency", prices)


async def gold():
    data = await get_gold_prices()

    prices = json.dumps(
        [item.model_dump() for item in data],
        ensure_ascii=False,
    )

    redis.set("tgju:gold", prices)


async def oil():
    data = await get_oil_prices()

    prices = json.dumps(
        [item.model_dump() for item in data],
        ensure_ascii=False,
    )

    redis.set("tgju:oil", prices)
