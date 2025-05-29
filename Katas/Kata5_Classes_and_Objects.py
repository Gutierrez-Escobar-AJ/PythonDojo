"""
🥋 Kata 5: Classes and Objects
📚 Build your own objects — and make your code smarter.
"""

# -----------------------------------------------------
# 🧠 Why Classes?
# Functions are great. But once your data grows (e.g., tasks, books, users),
# grouping everything into objects helps you stay organized.

# Think of classes like blueprints. You use them to build custom tools.
# -----------------------------------------------------

# -----------------------------------------------------
# 🏗️ 1. Creating a Basic Class
# -----------------------------------------------------

class Dog:
    def __init__(self, name, breed):
        self.name = name        # Attribute
        self.breed = breed      # Attribute

    def bark(self):             # Method
        return f"{self.name} says woof!"

# ✅ Usage
my_dog = Dog("Buddy", "Labrador")
print(my_dog.name)          # Access attribute → Buddy
print(my_dog.bark())        # Call method    → Buddy says woof!

# ✅ Concepts Used:
# - `class` defines a blueprint
# - `__init__` initializes data
# - `self` refers to the object itself
# - Attributes live inside `self`
# - Methods are functions tied to the object

# -----------------------------------------------------
# 🧱 2. Constructors vs Attributes
# -----------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def scale(self, factor):
        self.radius *= factor

c = Circle(5)
print(f"Original area: {c.area()}")  # → 78.54
c.scale(2)
print(f"Scaled area: {c.area()}")    # → 314.16

# -----------------------------------------------------
# 🔁 3. Combining Objects in a CLI Tool
# -----------------------------------------------------
# We'll now build a contact manager like Kata 3, but with class structure.
# Each contact is an object. The manager handles them as a collection.

# -----------------------------------------------------
# 🧪 Mini-Project: Contact Manager (Object-Oriented)
# -----------------------------------------------------

class Contact:
    """Represents a single contact."""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        """Return formatted contact string."""
        return f"{self.name}: {self.phone}"

class ContactManager:
    """Handles a list of contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        """Create and store a new contact."""
        new = Contact(name, phone)
        self.contacts.append(new)
        print(f"✅ Added contact: {new.display()}")

    def list_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts yet.")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.display()}")

    def find_contact(self, search_name):
        """Search for a contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                return contact
        return None

    def delete_contact(self, name):
        """Remove contact by name."""
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"❌ Deleted contact: {contact.name}")
        else:
            print("Contact not found.")

# -----------------------------------------------------
# 🧪 CLI App Runner
# -----------------------------------------------------

def run_contact_cli():
    manager = ContactManager()
    print("📇 Welcome to Contact Manager")

    while True:
        print("\nOptions: add, list, delete, quit")
        action = input("Choose an action: ").strip().lower()

        if action == "add":
            name = input("Name: ")
            phone = input("Phone: ")
            manager.add_contact(name, phone)

        elif action == "list":
            manager.list_contacts()

        elif action == "delete":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif action == "quit":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

# Run the program
run_contact_cli()

# -----------------------------------------------------
# 🧩 Summary:
# ✅ Classes let you combine data + behavior (attributes + methods)
# ✅ `__init__` sets up object state
# ✅ `self` is the object itself
# ✅ You used a CLI-based object tool — real world Python

# 🚀 You now have the tools to build full tools and pipelines — the dojo opens from here.
# -----------------------------------------------------

