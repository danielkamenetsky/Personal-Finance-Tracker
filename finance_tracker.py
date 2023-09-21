
# User Class represents a user in the system
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__transactions = []
    # This method allows a user to add a transaction to their list of transactions.

    def add_transaction(self, transaction):
        self.__transactions.append(transaction)
    # View all the transactions

    def view_transactions(self):
        return self.__transactions

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


class Expense(Transaction):
    def __init__(self, amount, description, category):
        super().__init__(amount, description)
        self.category = category  # e.g., Groceries, Entertainment, etc.

    def __str__(self):
        return f"Expense ({self.category}) - {super().__str__()}"
