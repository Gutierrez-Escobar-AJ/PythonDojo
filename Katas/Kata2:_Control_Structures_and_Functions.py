"""
🥋 Kata 2: Control Structures and Functions
📚 Make your code think with logic and flow.
"""

# -----------------------------------------------------
# 🧠 Real-World Analogy:
# Think of conditionals like traffic lights:
# If it's red, you stop. If it's green, you go. If it's yellow... you decide!
# In code, "if" is how your program makes decisions.
# -----------------------------------------------------

# -----------------------------------------------------
# 🔁 Step 1: Shorthand Operators
# These simplify math updates — like adding directly into a variable.
# -----------------------------------------------------

x = 5
x += 3  # Now x is 8
x -= 2  # Now x is 6
x *= 4  # Now x is 24
x /= 3  # Now x is 8.0 (a float)

print(f"After using shorthand operators, x is {x}")

# -----------------------------------------------------
# 🔍 Step 2: Multi-branch Conditional Logic
# Your program reacts differently depending on the input.
# -----------------------------------------------------

temperature = float(input("Enter the current temperature in Celsius: "))

if temperature < 0:
    print("It's freezing!")
elif 0 <= temperature < 10:
    print("It's cold.")
elif 10 <= temperature < 20:
    print("It's cool.")
elif 20 <= temperature < 30:
    print("It's warm.")
else:
    print("It's hot!")

# -----------------------------------------------------
# 🔁 Step 3: Looping with `for`
# For loops repeat a fixed number of times.
# -----------------------------------------------------

print("Counting from 1 to 5 using a for loop:")
for i in range(1, 6):
    print(i)

# -----------------------------------------------------
# 🔁 Step 4: Looping with `while`
# While loops repeat until a condition becomes false.
# -----------------------------------------------------

print("Counting down from 5 to 1 using a while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1

# -----------------------------------------------------
# 🔢 Step 5: Nested Loops — Multiplication Table
# Combining two loops builds grid-like logic.
# -----------------------------------------------------

print("Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end='\t')
    print()  # New line after each row

# -----------------------------------------------------
# ⚖️ Step 6: Conditional inside Loop — Print Even Numbers
# Conditionals inside loops help you filter or branch logic.
# -----------------------------------------------------

print("Even numbers between 1 and 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# -----------------------------------------------------
# 🔧 Step 7: Defining Functions
# Functions let us encapsulate and reuse code blocks.
# -----------------------------------------------------

def greet_user(name):
    """Greets the user with their name."""
    return f"Hello, {name}!"

user_name = input("Enter your name: ")
print(greet_user(user_name))

# -----------------------------------------------------
# 🔧 Step 8: Functions with Multiple Parameters
# Functions can do real work — like math!
# -----------------------------------------------------

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The sum is {add_numbers(num1, num2)}")

# -----------------------------------------------------
# 🔄 Step 9: Combining Functions + Loops
# Calculate factorial using a loop and a function
# -----------------------------------------------------

def factorial(n):
    """Returns factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")

# -----------------------------------------------------
# 🔍 Step 10: Check for Prime Numbers using Logic and Loops
# -----------------------------------------------------

def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# -----------------------------------------------------
# 🧪 Dojo Practice Reps (Mini Challenges)
# -----------------------------------------------------

# 🥋 Challenge 1: Voting Age Checker
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

# 🥋 Challenge 2: CLI Login Validator
# Hardcoded username and password (for simplicity)
valid_username = "dojo"
valid_password = "1234"

# Prompt user input
username = input("Username: ")
password = input("Password: ")

# Check credentials
if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Access denied.")

# -----------------------------------------------------
# 🧠 Mini Project: Password Strength Checker
# -----------------------------------------------------

"""
Goal: Practice everything from Kata 2 — input, conditionals, loops, functions, and string logic.

The tool will:
1. Ask the user to enter a password.
2. Evaluate if it's strong based on:
   - Length >= 8
   - Contains at least one digit
   - Contains at least one uppercase letter
3. Output strength status.
"""

def is_strong_password(password):
    """Returns True if the password is strong."""
    has_digit = False
    has_upper = False

    # Loop through each character to check conditions
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    # Return True only if all 3 conditions are met
    return len(password) >= 8 and has_digit and has_upper

# Step-by-step execution
password = input("Create a password: ")

if is_strong_password(password):
    print("✅ Your password is strong!")
else:
    print("❌ Your password is weak. Try again using at least 8 characters, one digit, and one uppercase letter.")

# -----------------------------------------------------
# 🧩 Summary:
# - You now control your code’s logic with if/else/elif.
# - You learned to repeat code with for/while loops.
# - You saw how functions help you reuse logic cleanly.
# - You solved real tasks using all of the above — just like toolmakers do.
# -----------------------------------------------------

