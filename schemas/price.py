from pydantic import BaseModel


# Base of PriceItem
class PriceItem(BaseModel):
    title: str
    price: str
    key: str


# Gold Schema
class CurrencyCategory(PriceItem):
    pass


# Gold Schema
class GoldCategory(BaseModel):
    title: str
    prices: list[PriceItem]
