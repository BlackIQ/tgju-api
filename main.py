# FastAPI
from fastapi import FastAPI

# Routers
from routers import price

# FastAPI instance
app = FastAPI(
    title="TGJU Scrapper API",
    version="1.1.0",
    summary="An API to scrap TGJU website data and share it with you using FastAPI.",
    contact={
        "name": "Amirhossein Mohammadi",
        "url": "https://amirhossein.info",
        "email": "hi@amirhossein.info",
    },
    openapi_tags=[
        {"name": "Price", "description": "TGJU scrapper endpoints for Gold & Currency"},
    ],
)

# Routers
app.include_router(price.router, prefix="/api")
