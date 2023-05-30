from api.main import app

from api.config.config import env

if __name__ == "__main__":
    app.run("0.0.0.0", port=env("PORT"), debug=True)
