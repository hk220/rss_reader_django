import time

class Item:
    def __init__(self, id: str = "", title: str = "", updated: str = "", updated_parsed: time.struct_time = None, link: str = "", summary: str = ""):
        self.id = id
        self.title = title
        self.updated = updated
        self.updated_parsed = updated_parsed
        self.link = link
        self.summary = summary
