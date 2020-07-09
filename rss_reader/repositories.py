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
            result.append(Item(entry.title, entry.updated, entry.link))
        return result


class RSSTestRepository(RSSRepositoryInterface):
    def fetch_items(self, url: str) -> List[Item]:
        return [Item('精錬イベントやRJSの準備など', '2020-06-30T18:00:36+09:00', 'http://ro-blog.livedoor.biz/archives/5658110.html')]
