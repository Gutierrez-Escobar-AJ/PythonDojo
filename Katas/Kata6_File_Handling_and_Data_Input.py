"""
🥋 Kata 6: File Handling & Data Input
📚 Teach your code to read, write, and manipulate files.
"""

# -----------------------------------------------------
# 🧠 Why Learn File I/O?
# Functions let us process input from the terminal.
# But real-world tools often work with files — logs, datasets, configs, etc.
# File I/O lets us read, process, write, and save data.
# -----------------------------------------------------

# -----------------------------------------------------
# 📂 1. Opening and Reading a File (Basic)
# -----------------------------------------------------

# This assumes there's a file named "sample.txt" in the same folder
# with a few lines of text in it.

# Always use `with` to open files — it automatically closes the file safely.
with open("sample.txt", "r") as file:
    content = file.read()
    print("📄 Full file content:")
    print(content)

# -----------------------------------------------------
# 🧾 2. Reading Line-by-Line
# -----------------------------------------------------

with open("sample.txt", "r") as file:
    print("\n📄 Reading line-by-line:")
    for line in file:
        print(line.strip())  # .strip() removes \n

# -----------------------------------------------------
# 🖋️ 3. Writing to a File
# -----------------------------------------------------

# Overwrites file if it exists, creates if not
with open("output.txt", "w") as file:
    file.write("Hello from Python Dojo!\n")
    file.write("This file was generated in Kata 6.\n")

print("\n✅ Wrote to output.txt")

# -----------------------------------------------------
# 📌 4. Appending to a File
# -----------------------------------------------------

with open("output.txt", "a") as file:
    file.write("This line was appended.\n")

print("✅ Appended to output.txt")

# -----------------------------------------------------
# 🧪 Mini-Project: CLI CSV Cleaner
# -----------------------------------------------------
"""
🎯 Goal: Build a command-line tool that:
- Loads a .csv file
- Removes empty lines or malformed rows
- Outputs a clean version to a new file

We'll simulate this with a basic CSV like:

name,age,email
Alice,30,alice@example.com
Bob,,bob@example.com
Charlie,25
,,
"""

INPUT_FILE = "contacts_dirty.csv"
OUTPUT_FILE = "contacts_cleaned.csv"

def is_valid_row(fields):
    """Returns True if all fields are non-empty."""
    return all(field.strip() != "" for field in fields)

def clean_csv(input_file, output_file):
    cleaned = []

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # Skip completely empty lines

            fields = line.split(",")
            if is_valid_row(fields):
                cleaned.append(fields)

    with open(output_file, "w") as f:
        for row in cleaned:
            f.write(",".join(row) + "\n")

    print(f"✅ Cleaned CSV saved to: {output_file}")
    print(f"🧼 {len(cleaned)} valid rows written.")

# -----------------------------------------------------
# 🏁 Run the CLI CSV cleaner
# -----------------------------------------------------

print("\n📂 Running CSV cleaner...")

try:
    clean_csv(INPUT_FILE, OUTPUT_FILE)
except FileNotFoundError:
    print("❌ Input file not found. Please create 'contacts_dirty.csv' first.")

# -----------------------------------------------------
# 🧩 Summary:
# ✅ You now know:
# - How to read and write files using `open()`
# - How to use `with` for automatic cleanup
# - How to validate and clean file content
# - How to build CLI tools that process file data
# -----------------------------------------------------

