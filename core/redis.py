# Libs
from redis.asyncio import Redis  # Redis

# Application
from core.settings import settings  # Core: Settings

redis = Redis.from_url(settings.redis_url, decode_responses=True)
