from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from typing import List, Dict

from .entities import Item
from .application_services import RSSItemApplicationService


def show(request: HttpRequest) -> HttpRequest:
    rss_item_application_service = RSSItemApplicationService()

    if request.method == "POST":
        feed_url: str = request.POST['feed_url']
        feed_items: List[Item] = rss_item_application_service.get_all_items(feed_url)
        context: Dict[str, List[Item]] = {"feed_items": feed_items}
        return render(request, "rss_reader/show.html", context=context)
    raise Exception("想定外のHTTPリクエストメソッドです")

def index(request: HttpRequest) -> HttpResponse:
        return render(request, "rss_reader/index.html")
