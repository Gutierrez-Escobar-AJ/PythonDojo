"""
🥋 Kata 1: Foundations of Python Programming
📚 Learn how to think in Python — variables, input/output, strings, and comments.
"""

# -----------------------------------------------------
# 🧠 Real-World Analogy:
# Think of variables like labeled post-it notes.
# You store values in them so Python can remember things while your program runs.
# -----------------------------------------------------

# Step 1: Creating and using basic variables

my_int = 10           # Integer type: whole number
my_float = 20.5       # Float type: decimal number
my_str = "Hello, Python!"  # String type: text

# Step 2: Outputting variables using print()
# This simulates how we display results to the terminal in a CLI program

print(my_int)      # Output: 10
print(my_float)    # Output: 20.5
print(my_str)      # Output: Hello, Python!

# Step 3: Combining different variable types into one message using formatted strings (f-strings)
message = f"{my_str} The number is {my_int} and the float is {my_float}."
print(message)

# -----------------------------------------------------
# 🧮 Arithmetic Operations
# Let's do some basic math with our variables.
# -----------------------------------------------------

sum_result = my_int + my_float       # Addition
product_result = my_int * 2          # Multiplication

print(f"Sum: {my_int} + {my_float} = {sum_result}")            # Output: 30.5
print(f"Product: {my_int} * 2 = {product_result}")             # Output: 20

# -----------------------------------------------------
# 💬 User Input: input() function
# Let's interact with the user — just like real CLI tools do.
# input() captures a string typed by the user in the terminal.
# -----------------------------------------------------

user_name = input("Enter your name: ")  # Prompt the user and store their input
greeting = f"Hello, {user_name}! Welcome to the Python Dojo."
print(greeting)

# Ask the user to enter two numbers and compute their sum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

# -----------------------------------------------------
# ✅ Conditional Logic: Making decisions with if/else
# -----------------------------------------------------

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# -----------------------------------------------------
# 🧩 Put it all together: full CLI interaction
# -----------------------------------------------------

user_name = input("What's your name? ")
age = int(input(f"Hi {user_name}, how old are you? "))
num1 = float(input(f"Please provide a number, {user_name}: "))
num2 = float(input("Please provide another number: "))
sum_result = num1 + num2

if age < 18:
    age_status = "a minor"
else:
    age_status = "an adult"

final_message = (
    f"Hello, {user_name}. You are {age} years old, which means you are {age_status}. "
    f"The sum of the numbers {num1} and {num2} is {sum_result}."
)
print(final_message)

# -----------------------------------------------------
# 🧪 Mini Challenges (Dojo Practice Reps)
# -----------------------------------------------------

# 🥋 Challenge 1: Age in Months + Minor or Adult Status
# Goal: Practice input(), arithmetic, if/else logic, formatted output.


# Step 1: Ask for the user's age
age_years = int(input("Enter your age in years: "))

# Step 2: Convert years to months
age_months = age_years * 12

# Step 3: Decide whether the user is a minor or an adult
if age_years < 18:
    status = "a minor"
else:
    status = "an adult"

# Step 4: Display the results using f-strings
print(f"You are {status}, and you have lived for approximately {age_months} months.")


# 🥋 Challenge 2:Odd or Even Checker
# Goal: Reinforce conditionals using the modulus operator (%), along with input() and print().


# Step 1: Ask for a number from the user
number = int(input("Enter any whole number: "))

# Step 2: Use modulus to determine odd/even
# The % operator returns the remainder; even numbers have no remainder when divided by 2
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

# Step 3: Output result
print(f"The number {number} is {result}.")

# -----------------------------------------------------
# 🔥 Tool Tease
# By the time you finish Kata 5, you'll be building your first file-processing CLI tools
# that can open, read, and analyze data — like a real Python professional.
# -----------------------------------------------------

# End of Kata 1

