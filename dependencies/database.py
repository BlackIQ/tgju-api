# Application
from core.database import session  # Database


# Get DB
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
