# TGJU API

Just a simple project to scrap [tgju.org](https://www.tgju.org). Here I just parse data and return them.

## Docs

You can use **Swagger** to test. [Open Swagger](https://app.swaggerhub.com/apis-docs/AMIRHOSSEINMOHAMMADI/TGJU/1.0.0).

## Notebook

The notebook is just for testing.

## API

So, I used notebooks as I said to scrap data. Now used it in an API.

### Routes

- baseUrl: [https://tgju.amirhossein.info/api](https://tgju.amirhossein.info/api)

Here are routes.

#### `/price/:of`

In `/price` route we have a param named `of`. This item can be one of items below:

- gold: To get gold prices
- currency: To get currencies prices

If `of` is not in the list, you will get 404 errror with this data:

```json
{
  "message": "Invalid"
}
```

Example:

- [https://tgju.amirhossein.info/api/price/gold](https://tgju.amirhossein.info/api/price/gold) -> Gold
- [https://tgju.amirhossein.info/api/price/currency](https://tgju.amirhossein.info/api/price/currency) -> Currency
