# Libs
from sqlalchemy import create_engine  # SQLAlchemy
from sqlalchemy.orm import sessionmaker  # SQLAlchemy ORM

# Application
from core.settings import settings  # Settings

# Create Engine
engine = create_engine(settings.postgresql_url, pool_pre_ping=True)

# Create Session
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
