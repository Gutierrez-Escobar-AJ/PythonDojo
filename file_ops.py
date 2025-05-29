import os
from session import ReadingSession
from utils import log_error


def load_log(path):
    sessions = []
    try:
        with open(path, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    name, book, pages, minutes, status = parts
                    session = ReadingSession(name, int(pages), int(minutes), status)
                    sessions.append(session)
    except FileNotFoundError:
        print("🕸️ No previous sessions found. Starting fresh.")
    except Exception as e:
        print("⚠️ Error loading log file.")
        log_error(str(e))
    return sessions


def save_log(path, sessions):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as file:
            for session in sessions:
                file.write(session.to_line() + "\n")
    except Exception as e:
        print("⚠️ Error saving to log file.")
        log_error(str(e))
