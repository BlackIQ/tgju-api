# Application
from core.database import session  # Core: Database


# Get DB
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
