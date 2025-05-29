from session import ReadingSession

class ReadingTracker:
    def __init__(self):
        self.log = []

    def add_session(self, session):
        self.log.append(session)

    def summary(self):
        print("\n📊 Reading Summary:")
        for i, s in enumerate(self.log, 1):
            print(f"\n📗 Session {i}")
            print(f"Name: {s.name}")
            print(f"Book: {s.book}")
            print(f"Pages: {s.pages}")
            print(f"Time: {s.minutes} min")
            print(f"Status: {s.status}")
