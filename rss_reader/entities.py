class Item:
    title: str = ""
    updated: str = ""
    link: str = ""

    def __init__(self, title: str, updated: str, link: str):
        self.title = title
        self.updated = updated
        self.link = link
