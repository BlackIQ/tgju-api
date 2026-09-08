from pydantic import BaseModel


class PriceItem(BaseModel):
    title: str
    price: str
    key: str
    status: str | None = None
    low_price: str | None = None
    high_price: str | None = None


class PriceCategory(BaseModel):
    title: str
    prices: list[PriceItem]
