
# User Class represents a user in the system
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__transactions = []
        self.__balance = 0  # Initialize balance to 0
    # This method allows a user to add a transaction to their list of transactions.

    def add_transaction(self, transaction):
        self.__transactions.append(transaction)
        # Update balance based on transaction type
        if isinstance(transaction, Income):
            self.__balance += transaction.amount
        elif isinstance(transaction, Expense):
            self.__balance -= transaction.amount
    # View all the transactions

    def view_transactions(self):
        return self.__transactions

    def view_transactions_by_category(self, category):
        # Start with an empty list for filtered transactions
        filtered_transactions = []

        # Go through each transaction in the user's transactions
        for t in self.__transactions:
            # Check if the transaction has a category and if that category matches the one we're looking for
            if hasattr(t, 'category') and t.category == category:
                # If it does, add it to our filtered transactions list
                filtered_transactions.append(t)
        return filtered_transactions

    def get_balance(self):
        # Return the current balance
        return self.__balance

    # Calculate total income and expense
    def summary(self):
        total_income = 0
        total_expense = 0

        # Loop through each transaction
        for transaction in self.__transactions:
            # Check if the transaction is of type Income
            if isinstance(transaction, Income):
                total_income += transaction.amount
            # Check if the transaction is of type Expense
            elif isinstance(transaction, Expense):
                total_expense += transaction.amount

        return {
            'Total Income': total_income,
            'Total Expense': total_expense,
            'Balance': self.__balance
        }

    def check_password(self, password):
        # Check if the given password matches the user's password
        return self.__password == password

    @property
    def username(self):
        return self.__username
# Transaction Class

# Class represents a financial transaction


class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.description}: ${self.amount}"

# Income and Expense Subclasses
# These classes represent an income transaction and inherit from the Transaction class
# In addition to attributes from Transaction class, it has a category attribute; Salary, Gift


class Income(Transaction):
    def __init__(self, amount, description, category):
        super().__init__(amount, description)
        self.category = category  # e.g., Salary, Gifts, etc.

    def __str__(self):
        return f"Income ({self.category}) - {super().__str__()}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount and self.description == other.description and self.category == other.category
        return False


class Expense(Transaction):
    def __init__(self, amount, description, category):
        super().__init__(amount, description)
        self.category = category  # e.g., Groceries, Entertainment, etc.

    def __str__(self):
        return f"Expense ({self.category}) - {super().__str__()}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount and self.description == other.description and self.category == other.category
        return False


class System:
    def __init__(self):
        self.__users = {}  # Dictionary to store users, with username as key and User object as value

    def register(self, username, password):
        if username in self.__users:
            print("Username already exists!")
            return None
        user = User(username, password)
        self.__users[username] = user
        print(f"User {username} registered successfully!")
        return user

    def login(self, username, password):
        user = self.__users.get(username)
        if not user:
            print("User not found!")
            return None
        # assuming you have a method in User class to check password
        if user.check_password(password):
            print(f"Welcome {username}!")
            return user
        else:
            print("Incorrect password!")
            return None

    def get_user(self, username):
        # Retrieve a User object by username
        return self.users.get(username)
# # Test
# # Create a user
# daniel = User("danielkamenetsky", "securepassword")

# # Add income and expense transactions
# daniel.add_transaction(Income(5000, "Monthly Salary", "Salary"))
# daniel.add_transaction(Expense(50, "Lunch", "Food"))
# daniel.add_transaction(Expense(200, "Shoes", "Shopping"))
# daniel.add_transaction(Income(100, "Gift", "Gifts"))

# # View transactions
# for transaction in daniel.view_transactions():
#     print(transaction)

# # Check balance
# print(f"Current Balance: ${daniel.get_balance()}")

# # Display a summary
# summary = daniel.summary()
# for key, value in summary.items():
#     print(f"{key}: ${value}")

# # Test viewing transactions by category
# food_transactions = daniel.view_transactions_by_category("Food")
# print("\nFood Transactions:")
# for transaction in food_transactions:
#     print(transaction)
