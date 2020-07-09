from typing import List
from .entities import Item
from .repository_interfaces import RSSRepositoryInterface
from .repositories import RSSRepository

class RSSItemApplicationService:
    rss_repository: RSSRepositoryInterface = RSSRepository()

    def get_all_items(self, feed_url: str) -> List[Item]:
        return self.rss_repository.fetch_items(feed_url)
