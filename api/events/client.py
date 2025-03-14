import aiohttp
import logging
import asyncio

from api.config import config

logger = logging.getLogger("uvicorn")

async def push_event(event_type, data):
    """Push an event to Survey with retry logic."""
    
    payload = {"hostId": config.HOST_NAME, "eventType": event_type, "data": data}
    headers = {"X-ACCESS-KEY": config.ACCESS_TOKEN, "X-HOST-KEY": config.HOST_TOKEN}
    
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=config.REQUEST_TIMEOUT)) as session:
        for attempt in range(config.MAX_RETRIES + 1):
            try:
                async with session.post(f"{config.SURVEY_URL}/api/events", json=payload, headers=headers) as resp:
                    if resp.status == 200:
                        logger.info(f"Pushed event {event_type} to Survey")
                        return True
                    else:
                        logger.error(f"Failed to push event {event_type}: {resp.status}")
            except Exception as e:
                logger.error(f"Error pushing event {event_type}: {str(e)}")
            
            if attempt < config.MAX_RETRIES:
                await asyncio.sleep(config.RETRY_DELAY)
        return False
