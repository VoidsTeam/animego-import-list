import aiohttp
import asyncio
import json
import os
from concurrent.futures import ProcessPoolExecutor
import time
from typing import Dict, Optional, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SHIKIMORI_API = "https://shikimori.one/api/animes"
RATE_LIMIT = 2

class AnimeCache:
    def __init__(self, cache_file: str = 'anime_id_cache.json'):
        self.cache_file = cache_file
        self.cache: Dict[str, Optional[int]] = self._load_cache()

    def _load_cache(self) -> Dict[str, Optional[int]]:
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.warning("Cache file corrupted, creating new cache")
                return {}
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def get(self, title: str) -> Optional[int]:
        return self.cache.get(title)

    def set(self, title: str, anime_id: Optional[int]):
        self.cache[title] = anime_id
        if len(self.cache) % 50 == 0:
            self.save_cache()

class ShikimoriAPI:
    def __init__(self, pool_size=3):
        self.sessions = []
        self.last_request_times = []
        self.pool_size = pool_size
        self.current_session = 0

    async def init_session(self):
        if not self.sessions:
            for _ in range(self.pool_size):
                session = aiohttp.ClientSession(headers={
                    'User-Agent': 'AnimeListConverter/2.0',
                    'Accept': 'application/json'
                })
                self.sessions.append(session)
                self.last_request_times.append(0)

    async def close_session(self):
        for session in self.sessions:
            await session.close()
        self.sessions = []

    async def search_anime(self, title: str) -> Optional[int]:
        await self.init_session()

        session_idx = self.current_session
        self.current_session = (self.current_session + 1) % self.pool_size
        
        current_time = time.time()
        time_since_last = current_time - self.last_request_times[session_idx]
        if time_since_last < RATE_LIMIT:
            await asyncio.sleep(RATE_LIMIT - time_since_last)
        
        try:
            params = {'search': title, 'limit': 1}
            async with self.sessions[session_idx].get(SHIKIMORI_API, params=params) as response:
                self.last_request_times[session_idx] = time.time()
                
                if response.status == 429:
                    logger.warning("Rate limit hit, waiting 60 seconds...")
                    await asyncio.sleep(60)
                    return await self.search_anime(title)
                
                if response.status == 200:
                    results = await response.json()
                    if results:
                        return results[0]['id']

        
        except Exception as e:
            logger.error(f"Error searching for '{title}': {e}")
        
        return None

async def update_anime_ids(json_file: str):
    logger.info("Starting ID update process...")
    
    cache = AnimeCache()
    api = ShikimoriAPI(pool_size=3)
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = len(data)
    updated = 0
    
    for i, item in enumerate(data):
        if item['target_id'] == 0:
            title = item['target_title_eng']
            if title not in cache.cache:
                anime_id = await api.search_anime(title)
                if anime_id:
                    item['target_id'] = anime_id
                    cache.set(title, anime_id)
                    updated += 1
                    logger.info(f"Processed {i + 1}/{total}: Found ID {anime_id} for {title}")
                else:
                    logger.info(f"ID not found for {title}")
            else:
                anime_id = cache.get(title)
                if anime_id:
                    item['target_id'] = anime_id
                    updated += 1
                    logger.info(f"Using cached ID {anime_id} for {title}")
    
    await api.close_session()
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    cache.save_cache()
    logger.info(f"Updated {updated} entries")

def main():
    json_file = 'shikimori_import.json'
    asyncio.run(update_anime_ids(json_file))

if __name__ == "__main__":
    main()
