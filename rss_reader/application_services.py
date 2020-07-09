from typing import List
import inject

from .entities import Item
from .repository_interfaces import RSSRepositoryInterface

class RSSApplicationService:
    rss_repository: RSSRepositoryInterface = inject.attr(RSSRepositoryInterface)

    def get_all_items(self, feed_url: str) -> List[Item]:
        return self.rss_repository.fetch_items(feed_url)
