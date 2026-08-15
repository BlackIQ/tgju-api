# Libs
from fastapi import FastAPI  # FastAPI
from fastapi.middleware.cors import CORSMiddleware  # FastAPI CORS

# Application
from routers import price  # Routers

# FastAPI instance
app: FastAPI = FastAPI(
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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[
        "https://tgju.amirhossein.info",
        "http://localhost:3000",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
    ],
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)


# Routers
app.include_router(price.router, prefix="/api")
