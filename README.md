# 🥋 Python Dojo — Learn Python by Building a Real CLI Tool

**Welcome to the Dojo.**  
This is the official code repository for the ebook:  
📘 _Python Dojo for Beginners__if you read me, you built me_

<p align="center">
  <img src="logo/logo.png" alt="Python Dojo Logo" width="350"/>
</p>

If you're learning Python and want to build something real while you learn — this is your starting point.  
Each chapter of the book evolves a **Reading Tracker CLI tool**. You’ll write the code step by step, level by level, like a martial arts kata.

> ❝ If you read me, you built me. ❞

---

## 📦 What You’ll Build

A complete command-line tool that lets you:

✅ Log your daily coding & reading progress  
✅ Save your sessions to a local file  
✅ Load and review your past progress  
✅ Handle errors and log them like a real developer  
✅ Structure your project with reusable modules  
✅ Run it like a real command-line program

---

## 📚 Chapters as Milestones

Each chapter of the book corresponds to a functional evolution of the tool:

| Chapter | Focus | What You Learn |
|--------|-------|----------------|
| 1–2 | Hello World + Input | Basic I/O, strings, user interaction |
| 3 | Types | Working with numbers and text |
| 4 | Loops | Repetition and user control |
| 5 | Functions | Clean code, reusable logic |
| 6 | Classes | Organizing data with objects |
| 7 | File Handling | Reading and writing `.txt` files |
| 8 | Error Logging | Try/except, logging, and resilience |
| 9 | Tool Packaging | Modules, `main.py`, and project structure |

---

## 🛠️ How to Run the Tool

Make sure you have Python 3 installed.  
Then open your terminal and run:

```bash
python ReadingDojoTracker/main.py
```

📌 If you see an error about `data/reading_log.txt` or `logs/error_log.txt`, make sure the `data/` and `logs/` folders exist. The tool will create them after Chapter 9 improvements.

---

## 🧠 For Beginners, By a Sensei Who’s Been There

This project isn’t just about code. It’s about learning how to:

- Think like a developer
- Train with purpose
- Build something that matters to *you*

If you’re tired of tutorials that go nowhere, this is your dojo.

---

## ✨ Features at a Glance

- Simple CLI interface for beginners
- Clean modular design (no spaghetti code!)
- Real-world file handling (read/write)
- Built-in error handling and logging
- A growth mindset baked into the code

---

## 📁 Project Structure

```
ReadingDojoTracker/
├── main.py               # Entry point
├── tracker.py            # Manages the reading log
├── session.py            # Defines a single ReadingSession
├── file_ops.py           # Save/load to file
├── utils.py              # Logging and helpers
├── data/                 # Saves your reading_log.txt
└── logs/                 # Stores error_log.txt
```

---

## 🙌 Join the Dojo

If this project helped you learn Python,  
consider giving the repo a ⭐, sharing your version, or showing others what you built.

You can also follow the full journey in the ebook:  
**_Python Dojo for Beginners_** – coming soon on Gumroad.

---

## 🧘‍♂️ License

MIT — Free to learn, share, remix, and teach.  
Just don’t forget to bow when you fork. 🥋

---

_Ossu, coder. You made it this far.  
Now open the terminal and begin._
