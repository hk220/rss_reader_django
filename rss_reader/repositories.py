from typing import Protocol, List
from .entities import Item
from .repository_interfaces import RSSRepositoryInterface

import feedparser
import inject


class RSSRepository(RSSRepositoryInterface):
    def fetch_items(self, url: str) -> List[Item]:
        f: feedparser.FeedParserDict = feedparser.parse(url)
        result: List[Item] = []
        for entry in f.entries:
            result.append(Item(entry.id, entry.title, entry.updated, entry.updated_parsed, entry.link, entry.summary))
        return result
