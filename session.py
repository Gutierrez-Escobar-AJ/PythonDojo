class ReadingSession:
    def __init__(self, name, pages, minutes, status):
        self.name = name
        self.book = "Python Dojo"
        self.pages = pages
        self.minutes = minutes
        self.status = status

    def to_dict(self):
        return {
            "name": self.name,
            "book": self.book,
            "pages": self.pages,
            "minutes": self.minutes,
            "status": self.status
        }

    def to_line(self):
        return f"{self.name}|{self.book}|{self.pages}|{self.minutes}|{self.status}"






