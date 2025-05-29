
"""
🥋 Kata 7: Error Handling & Logging
📚 Catch mistakes, log them, and don’t crash.
"""

# -----------------------------------------------------
# 🧠 Why Learn Error Handling?
# Errors crash programs. Catching them = writing resilient tools.
# Logging = recording what happened and when (like a black box).
# -----------------------------------------------------

# -----------------------------------------------------
# 🔍 1. try, except, finally
# -----------------------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} = {result}")
except ValueError:
    print("❌ That wasn't a valid number.")
except ZeroDivisionError:
    print("❌ You can't divide by zero.")
finally:
    print("🧹 This runs no matter what (cleanup or closing logic).")

# -----------------------------------------------------
# 🧱 2. Common Python Exceptions
# -----------------------------------------------------
# - ValueError → Wrong type conversion
# - IndexError → Accessing out-of-range list index
# - FileNotFoundError → File doesn’t exist
# - TypeError → Wrong type passed to a function
# - ZeroDivisionError → Division by 0

def cause_errors():
    # IndexError example
    try:
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
    except IndexError:
        print("⚠️ IndexError: Index is out of bounds.")

    # ValueError example
    try:
        age = int("not_a_number")  # ValueError
    except ValueError:
        print("⚠️ ValueError: Cannot convert to integer.")

    # FileNotFoundError example
    try:
        with open("non_existent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("⚠️ FileNotFoundError: File doesn't exist.")

    # TypeError example
    try:
        result = "5" + 5  # TypeError
    except TypeError:
        print("⚠️ TypeError: Cannot add string and integer.")

    # ZeroDivisionError example
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("⚠️ ZeroDivisionError: Cannot divide by zero.")

cause_errors()

# -----------------------------------------------------
# 📓 3. Writing Logs to a File
# -----------------------------------------------------

def log_error(message):
    """Append error message to log file with timestamp."""
    from datetime import datetime
    with open("error_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

# -----------------------------------------------------
# 🧪 Mini-Project: CLI Form Validator + Logger
# -----------------------------------------------------
"""
🎯 Goal: Build a CLI app that:
- Prompts user for name, age, and email
- Validates each input
- Logs errors to a .txt file
- Finishes cleanly even if errors occur
"""

def validate_name(name):
    if len(name.strip()) < 2:
        raise ValueError("Name too short.")
    return name.strip()

def validate_age(age_str):
    age = int(age_str)
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return age

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email must contain '@' and '.'")
    return email.strip()

def run_validator():
    print("\n📋 Welcome to the CLI Form Validator")

    try:
        name = validate_name(input("Enter your name: "))
        age = validate_age(input("Enter your age: "))
        email = validate_email(input("Enter your email: "))

    except ValueError as e:
        print(f"❌ Validation error: {e}")
        log_error(f"Validation failed: {e}")
    except Exception as e:
        print("❌ Unexpected error.")
        log_error(f"Unknown error: {e}")
    else:
        print("\n✅ Form submitted successfully!")
        print(f"Name: {name}, Age: {age}, Email: {email}")
    finally:
        print("🧹 Closing validator.")

# Run the form
run_validator()

# -----------------------------------------------------
# 🧩 Summary:
# ✅ You now know:
# - How to prevent crashes using try/except/finally
# - How to catch and handle common exceptions
# - How to log problems to a file for debugging
# - How to apply it all in a real CLI tool
# -----------------------------------------------------
