"""
🥋 Kata 3: Working with Basic Data Structures and Control Flow
📚 Learn how to store, sort, search, and loop with control.
"""

# -----------------------------------------------------
# 🧠 Real-World Analogies
# -----------------------------------------------------
# - List = a row of labeled lockers (ordered, changeable)
# - Tuple = a locked briefcase (ordered, unchangeable)
# - Dict = a phonebook (key → value lookup)
# - Set = a box of unique items (no duplicates allowed)

# -----------------------------------------------------
# 🧺 1. Lists — Locker Rows
# -----------------------------------------------------

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")         # Add to the end
fruits.insert(1, "kiwi")        # Insert at position
fruits[0] = "grape"             # Modify
del fruits[2]                  # Delete by index
print("grape" in fruits)       # Check if exists
print(fruits)

# Loop through
for fruit in fruits:
    print(f"One fruit: {fruit}")

# List comprehension (transform)
upper_fruits = [f.upper() for f in fruits]
print(upper_fruits)

# Sorting, slicing, copying
fruits.sort()
print(fruits[:2])               # First 2
copied = fruits.copy()

# -----------------------------------------------------
# 🏫 2. Tuples — Immutable Groups
# -----------------------------------------------------

coordinates = (10, 20)
x, y = coordinates              # Tuple unpacking
print(f"x = {x}, y = {y}")

def get_bounds(values):
    return min(values), max(values)

nums = [3, 5, 2, 8]
lo, hi = get_bounds(nums)
print(f"Range: {lo} to {hi}")

# -----------------------------------------------------
# ☎️ 3. Dictionaries — Phonebooks
# -----------------------------------------------------

person = {"name": "Alice", "age": 25}
person["email"] = "alice@example.com"
print(person.get("city", "Not found"))    # .get() = safe lookup
del person["age"]                         # Delete key
print("email" in person)                  # Check key
for key, val in person.items():
    print(f"{key}: {val}")

# Merge dictionaries
person.update({"city": "NYC", "job": "Dev"})

# -----------------------------------------------------
# 🎯 4. Sets — Unique Collections
# -----------------------------------------------------

colors = {"red", "blue", "green"}
colors.add("yellow")
colors.discard("blue")        # Safe remove
print("red" in colors)        # Membership test
print(colors.union({"black", "white"}))   # Combine

# -----------------------------------------------------
# 🔄 5. Control Flow: Loops
# -----------------------------------------------------

# For loop — use when you know how many times
for i in range(3):
    print(f"For loop: iteration {i+1}")

# While loop — use when condition-based
count = 0
while count < 3:
    print(f"While loop: count is {count}")
    count += 1

# ⚠️ Infinite loop warning
# Be cautious: forgetting to update the loop variable or break condition
# can trap you in an infinite loop that never ends.
# Example:
# while True:
#     print("Oops — infinite!")
#     break  # Safely exit

# -----------------------------------------------------
# 🧪 Mini-Challenge: Mixed Bag Analyzer
# -----------------------------------------------------
"""
Build a tool that:
- Accepts a string from the user
- Counts how many letters, digits, and symbols it has
- Uses for loop and if/else conditions
- Uses dictionary to summarize counts
"""

user_input = input("Enter a sentence with letters, numbers, and symbols: ")

summary = {"letters": 0, "digits": 0, "symbols": 0}

for char in user_input:
    if char.isalpha():
        summary["letters"] += 1
    elif char.isdigit():
        summary["digits"] += 1
    else:
        summary["symbols"] += 1

print("\nCharacter Summary:")
for key, value in summary.items():
    print(f"{key.title()}: {value}")

# -----------------------------------------------------
# 🪡 Summary:
# - Lists = mutable, ordered — like locker rows
# - Tuples = immutable, great for unpacking or returns
# - Dicts = key-value maps — like phonebooks
# - Sets = unordered, no duplicates — perfect for filtering
# - Loops = repeat action while a condition is met or for a known range
# - You used them to analyze input, control flow, and summarize info
# -----------------------------------------------------

# -----------------------------------------------------

