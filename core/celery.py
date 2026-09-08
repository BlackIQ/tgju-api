# Libs
from celery import Celery  # Celery

# Application
from core.settings import settings  # Core: Settings

# Celery jooooon
celery = Celery(
    "tgju",
    broker=settings.rabbitmq_url,
    backend=settings.redis_url,
)


# Config Celery
celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    imports=("tasks.price",),
)

# Config Beat
celery.conf.beat_schedule = {
    "update-prices-every-5-seconds": {
        "task": "tgju.update_prices",
        "schedule": 5.0,
    },
}
