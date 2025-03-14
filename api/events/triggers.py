from datetime import datetime
import sqlite3
import aiohttp
import logging

from api.config import config

logger = logging.getLogger("uvicorn")
DB_PATH = f"{config.PROJECT_DIRECTORY}/db/triggers.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS triggers (
        name TEXT PRIMARY KEY,
        input TEXT,
        condition TEXT,
        message TEXT
    )
""")
conn.commit()

last_trigger_update = None

async def sync_triggers():
    """Sync triggers from Cloud API every TRIGGER_UPDATE_INTERVAL."""
    
    global last_trigger_update
    if not last_trigger_update or (datetime.now() - last_trigger_update).total_seconds() > config.TRIGGER_UPDATE_INTERVAL:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=config.REQUEST_TIMEOUT)) as session:
            headers = {"X-ACCESS-KEY": config.ACCESS_TOKEN}
            try:
                async with session.get(f"{config.SURVEY_URL}/api/triggers", headers=headers) as resp:
                    if resp.status == 200:
                        triggers = await resp.json()
                        cursor.execute("DELETE FROM triggers")
                        for trigger in triggers:
                            cursor.execute(
                                "INSERT OR REPLACE INTO triggers (name, input, condition, message) VALUES (?, ?, ?, ?)",
                                (trigger["name"], trigger["input"], trigger["condition"], trigger["message"])
                            )
                        conn.commit()
                        last_trigger_update = datetime.now()
                        logger.info("Updated triggers from Cloud API")
                    else:
                        logger.error(f"Failed to fetch triggers: {resp.status}")
            except Exception as e:
                logger.error(f"Error syncing triggers: {str(e)}")

def get_triggers():
    """Load triggers from SQLite."""
    
    cursor.execute("SELECT name, input, condition, message FROM triggers")
    return cursor.fetchall()
