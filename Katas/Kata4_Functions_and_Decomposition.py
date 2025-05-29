"""
🥋 Kata 4: Functions and Decomposition
📚 Learn how to think in reusable blocks — input, output, purpose.
"""

# -----------------------------------------------------
# 🧠 Why Functions Matter
# Functions are the *organs* of your code: each one does one job, and they work together.
# A clean function system = maintainable, testable, expandable code.
# -----------------------------------------------------

# -----------------------------------------------------
# 🔧 1. Defining a Basic Function
# -----------------------------------------------------

def greet(name):
    return f"Hello, {name}!"

print(greet("Python Dojo"))  # Output: Hello, Python Dojo!

# ✅ Concepts:
# - `def` defines a function
# - `name` is a parameter
# - `return` sends back a result

# -----------------------------------------------------
# 🔁 2. Adding Arguments and Return Values
# -----------------------------------------------------

def add(x, y):
    return x + y

print(f"2 + 3 = {add(2, 3)}")

# -----------------------------------------------------
# ⚙️ 3. Default Values for Parameters
# -----------------------------------------------------

def welcome(name="coder"):
    return f"Welcome, {name}!"

print(welcome())           # → Welcome, coder!
print(welcome("Sarah"))    # → Welcome, Sarah!

# -----------------------------------------------------
# 🔁 4. Positional vs Keyword Arguments
# -----------------------------------------------------

def format_name(first, last):
    return f"{last}, {first}"

print(format_name("Ada", "Lovelace"))             # Positional
print(format_name(last="Einstein", first="Albert"))  # Keyword

# -----------------------------------------------------
# 🪓 5. Function Decomposition
# Break big problems into smaller pieces.
# -----------------------------------------------------

def clean_input(prompt):
    """Prompt user and strip whitespace."""
    return input(prompt).strip()

def is_valid_number(value):
    """Check if value can be converted to float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_valid_number(prompt):
    """Loop until user inputs a valid float."""
    while True:
        raw = clean_input(prompt)
        if is_valid_number(raw):
            return float(raw)
        print("❌ Not a number. Try again.")

# -----------------------------------------------------
# 🔁 6. Function Chaining
# -----------------------------------------------------

def square(x):
    return x * x

def add_five(x):
    return x + 5

print(add_five(square(3)))  # (3^2 = 9) + 5 → 14

# -----------------------------------------------------
# 🧠 7. Nested Functions (Light Touch)
# -----------------------------------------------------

def outer(name):
    def inner():
        return f"Hi, {name}"
    return inner()

print(outer("Student"))

# -----------------------------------------------------
# 💡 8. Higher-Order Functions (Preview)
# -----------------------------------------------------

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x + 1, 3))  # ((3 + 1) + 1) → 5

# -----------------------------------------------------
# 🧪 Mini-Project: CLI Expense Tracker
# -----------------------------------------------------
"""
🎯 Goal: Use function decomposition to build a terminal tool that tracks expenses.

🧩 Structure:
- get_expense(): get user input
- validate_expense(): check it's valid
- add_expense(): add to list
- total_expenses(): calculate total
- show_report(): print all
"""

expenses = []

def get_expense():
    """Prompt user for a new expense amount."""
    return input("Enter expense amount (or 'done'): ").strip()

def validate_expense(value):
    """Return float if valid, else None."""
    try:
        return float(value)
    except ValueError:
        return None

def add_expense(amount):
    """Append valid expense to list."""
    expenses.append(amount)

def total_expenses():
    """Sum all current expenses."""
    return sum(expenses)

def show_report():
    """Print all expenses and total."""
    print("\n📊 Expense Report")
    for i, amount in enumerate(expenses, start=1):
        print(f"{i}. ${amount:.2f}")
    print(f"Total: ${total_expenses():.2f}\n")

# 🧪 Run CLI Tool
print("\n💸 Welcome to the Expense Tracker\n")

while True:
    entry = get_expense()
    if entry.lower() == "done":
        break

    amount = validate_expense(entry)
    if amount is not None:
        add_expense(amount)
        print(f"✅ Added ${amount:.2f}")
    else:
        print("❌ Invalid input. Try again.")

show_report()

# -----------------------------------------------------
# 🧩 Summary:
# ✅ You now know:
# - How to define and call functions
# - How to validate and pass data between them
# - How to structure your code into small, clear units
# - How to reuse logic like a pro

# 💡 In Kata 5, you’ll learn to create classes — reusable blueprints for real-world objects and tools.
# -----------------------------------------------------

