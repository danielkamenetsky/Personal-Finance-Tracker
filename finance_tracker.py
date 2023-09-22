
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
