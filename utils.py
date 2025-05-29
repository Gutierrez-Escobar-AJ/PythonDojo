import os
import datetime

def get_feedback(pages, status):
    if pages > 10:
        session_type = "🔥 That was a focus session! Well done."
    elif pages > 0:
        session_type = "✅ Nice! Even a small session adds up."
    else:
        session_type = "📌 No pages today? No worries. Show up again tomorrow."

    if status == "new":
        status_msg = "🆕 Great, you’re moving forward."
    elif status == "reread":
        status_msg = "🔁 Mastery takes repetition. Well done."
    elif status == "recommend":
        status_msg = "💬 Share the wisdom!"
    else:
        status_msg = "❓ Unrecognized status — we'll count it as 'new'."

    return session_type, status_msg


def log_error(error_message):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "error_log.txt")
    with open(log_path, "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {error_message}\n")
