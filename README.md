# TGJU API

An API to scrap [tgju.org](https://www.tgju.org) and share it with you written in **FastAPI**.

## Docs

As this is a **FastAPI** application, you can checkout both Swagger and Redoc documentations.

- [Open Redoc](https://tgju.amirhossein.info/redoc).
- [Open Swagger](https://tgju.amirhossein.info/docs).

## Example

Each item has a schema like this:

```json
{
  "title": "دینار کویت",
  "price": "6,045,600",
  "key": "price_kwd",
  "status": "low",
  "low_price": "6,024,800",
  "high_price": "6,097,600"
}
```

- **title**: Name of item
- **price**: Price of course
- **key**: Slug of the item
- **status**: Is it low or high (Issue: https://github.com/BlackIQ/tgju-api/issues/1)
- **low_price**: Lowest price (Issue: https://github.com/BlackIQ/tgju-api/issues/1)
- **high_price**: Highest price (Issue: https://github.com/BlackIQ/tgju-api/issues/1)

Currently this app only supports **Currency** and **Gold**. So, checkout examples

### Gold

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

### Currency

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

## Notebook

> Notebooks are removed. But soon they'll be here again.

---

Thanks to @fatehi-develop for his idea about how, high and status.
