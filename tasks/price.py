# Libs
import asyncio  # AsyncIO

# Application
from core.celery import celery  # Core: Celery
from services.price import (
    currency,
    gold,
    oil,
)  # Services: TGJU


async def update_prices_async():
    await asyncio.gather(
        currency(),
        gold(),
        oil(),
    )


@celery.task(name="tgju.update_prices")
def update_prices():
    asyncio.run(update_prices_async())
