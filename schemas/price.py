from pydantic import BaseModel


# Base of PriceItem
class PriceItem(BaseModel):
    title: str
    price: str
    key: str
    status: str | None = None
    low_price: str | None = None
    high_price: str | None = None


# Gold Schema
class CurrencyCategory(PriceItem):
    pass


# Gold Schema
class GoldCategory(BaseModel):
    title: str
    prices: list[PriceItem]
