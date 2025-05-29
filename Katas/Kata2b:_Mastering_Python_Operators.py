"""
🥋 Kata 2b: Mastering Python Operators
📚 Learn to calculate, compare, and control with operators.
"""

# -----------------------------------------------------
# 🧠 Operator Categories: Mental Map
# -----------------------------------------------------
# | Category        | Operators                         |
# |----------------|------------------------------------|
# | Arithmetic      | + - * / // % **                   |
# | Comparison      | == != > < >= <=                   |
# | Logical         | and or not                        |
# | Assignment      | = += -= *= /= //= %= **=          |
# | Bitwise         | & | ^ ~ << >>                     |
# | Identity        | is is not                         |
# | Membership      | in not in                         |

# We’ll explore each type with examples and explain how they’re useful in tools.

# -----------------------------------------------------
# 1. Arithmetic Operators
# Used for math calculations
# -----------------------------------------------------

a, b = 5, 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus (reminder): {a % b}")     # 🔄 Tool Use: Useful for timers (e.g., repeat every 5)
print(f"Exponentiation: {a ** b}")

# -----------------------------------------------------
# 2. Comparison Operators
# Used in conditions to check equality or magnitude
# -----------------------------------------------------

print(f"Equal: {a == b}")
print(f"Not Equal: {a != b}")
print(f"Greater: {a > b}")
print(f"Less or Equal: {a <= b}")

# -----------------------------------------------------
# 3. Logical Operators
# Combine boolean expressions
# -----------------------------------------------------

x, y = True, False
print(f"AND: {x and y}")
print(f"OR: {x or y}")
print(f"NOT: {not x}")

# -----------------------------------------------------
# 4. Assignment Operators
# Update variables using shorthand
# -----------------------------------------------------

x = 10
x += 2
x *= 3
x %= 4
print(f"Chained Assignment: {x}")

# -----------------------------------------------------
# 5. Bitwise Operators (Binary logic)
# 🔄 Tool Use: Useful for flags, feature toggles, bit masking
# -----------------------------------------------------

x, y = 5, 3  # 0101 and 0011
print(f"Bitwise AND: {x & y}")
print(f"Bitwise OR: {x | y}")
print(f"Bitwise XOR: {x ^ y}")
print(f"Bitwise NOT: {~x}")
print(f"Left Shift: {x << 1}")
print(f"Right Shift: {x >> 1}")

# -----------------------------------------------------
# 6. Identity and Membership
# -----------------------------------------------------

lst = [1, 2, 3]
copy = lst
new = [1, 2, 3]

print(f"Identity: lst is copy → {lst is copy}")   # True
print(f"Identity: lst is new → {lst is new}")     # False
print(f"Membership: 2 in lst → {2 in lst}")       # True

# -----------------------------------------------------
# 🧪 Dojo Practice Reps
# -----------------------------------------------------

# ✅ Challenge: Timer Check
minute = 15
if minute % 5 == 0:
    print("⏰ Time for a break!")  # Modulus for repeating events

# ✅ Challenge: Bitwise Flag Checker
flags = 0b1010  # Binary: feature A and C are ON
mask_B = 0b0010
if flags & mask_B:
    print("🔒 Feature B is enabled.")
else:
    print("🔓 Feature B is off.")

# -----------------------------------------------------
# 🧠 Mini-Project: CLI Arithmetic Quiz App
# -----------------------------------------------------
"""
🎯 Objective:
Create a math quiz app using:
- input/output
- arithmetic
- comparison
- conditional logic
- scoring
- modulus (bonus: reward message every 3 questions)

📦 Concepts from this Kata:
Operators (arithmetic, comparison, logical, assignment)
"""

def quiz_question(q_num, num1, num2, operator, correct_answer):
    """Displays a math question and checks the user's answer."""
    print(f"\nQuestion {q_num}: What is {num1} {operator} {num2}?")
    user_answer = float(input("Your answer: "))
    
    if user_answer == correct_answer:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Incorrect. The correct answer is {correct_answer}")
        return False

# Initialize score
score = 0

# Run 5 quiz questions
for i in range(1, 6):
    if i == 1:
        if quiz_question(i, 5, 3, '+', 5 + 3): score += 1
    elif i == 2:
        if quiz_question(i, 10, 2, '-', 10 - 2): score += 1
    elif i == 3:
        if quiz_question(i, 4, 3, '*', 4 * 3): score += 1
    elif i == 4:
        if quiz_question(i, 12, 4, '/', 12 / 4): score += 1
    elif i == 5:
        if quiz_question(i, 2, 3, '**', 2 ** 3): score += 1
    
    # Bonus: Every 3rd question, give a motivational message
    if i % 3 == 0:
        print("🔥 Keep going, you’re doing great!")

# Final score
print(f"\n🎯 Final Score: {score}/5")
if score == 5:
    print("🥇 Perfect Score! You're a math ninja.")
elif score >= 3:
    print("👍 Good job! Keep practicing.")
else:
    print("👀 Time to review your operators!")

# -----------------------------------------------------
# 🧩 Summary:
# - You learned 7 types of operators with tool-focused logic.
# - You used operators in timers, flags, and a CLI quiz tool.
# - Operators are not just math — they control your code’s decisions.
# -----------------------------------------------------

