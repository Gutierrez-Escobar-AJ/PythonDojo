from session import ReadingSession
from tracker import ReadingTracker
from file_ops import load_log, save_log
from utils import get_feedback, log_error


def main():
    tracker = ReadingTracker()
    save_path = "data/reading_log.txt"
    tracker.log = load_log(save_path)

    while True:
        print("\n📚 New Reading Entry:")
        name = input("👋 Your name: ")

        try:
            pages = int(input("📄 Pages read: "))
            minutes = int(input("⏱️ Time coding: "))
        except ValueError as e:
            print("❌ Please enter valid numbers.")
            log_error(str(e))
            continue

        status = input("📌 Status ([new], [reread], [recommend]): ").lower()
        session_type, status_msg = get_feedback(pages, status)

        print(f"\n{session_type}")
        print(status_msg)

        session = ReadingSession(name, pages, minutes, status)
        tracker.add_session(session)

        save_log(save_path, tracker.log)

        cont = input("\n➕ Add another entry? (y/n): ").lower()
        if cont != "y":
            break

    tracker.summary()


if __name__ == "__main__":
    main()
