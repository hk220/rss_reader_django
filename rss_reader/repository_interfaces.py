from typing import Protocol, List
from .entities import Item


class RSSRepositoryInterface(Protocol):
    def fetch_items(self, url: str) -> List[Item]:
        ...
