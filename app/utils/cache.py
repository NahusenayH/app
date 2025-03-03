from datetime import datetime, timedelta
from typing import Any, Dict, Optional

class Cache:
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}

    def set(self, key: str, value: Any, expires_in: int) -> None:
        self._cache[key] = {
            'value': value,
            'expires_at': datetime.utcnow() + timedelta(seconds=expires_in)
        }

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        
        item = self._cache[key]
        if datetime.utcnow() > item['expires_at']:
            del self._cache[key]
            return None
            
        return item['value']

    def delete(self, key: str) -> None:
        if key in self._cache:
            del self._cache[key]

cache = Cache()