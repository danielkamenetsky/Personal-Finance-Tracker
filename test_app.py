import unittest
from app import User, Income, Expense, System


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def test_register_and_login(self):
        # Test registration
        user = self.system.register("danielkamenetsky", "securepassword")
        self.assertIsInstance(user, User)

        # Test registration with same username
        duplicate_user = self.system.register(
            "danielkamenetsky", "anotherpassword")
        self.assertIsNone(duplicate_user)

        # Test login with correct credentials
        logged_in_user = self.system.login(
            "danielkamenetsky", "securepassword")
        self.assertIsInstance(logged_in_user, User)

        # Test login with incorrect credentials
        wrong_user = self.system.login("danielkamenetsky", "wrongpassword")
        self.assertIsNone(wrong_user)

        # Test login with non-existing user
        non_existing_user = self.system.login(
            "nonexistentuser", "somepassword")
        self.assertIsNone(non_existing_user)


print("-----------------------------------------------------------------------\n")


class TestPersonalFinanceTracker(unittest.TestCase):

    def setUp(self):
        # Setup code: This runs before every test
        self.daniel = User("danielkamenetsky", "securepassword")

    def test_add_transaction(self):
        self.daniel.add_transaction(Income(5000, "Monthly Salary", "Salary"))
        self.daniel.add_transaction(Expense(50, "Lunch", "Food"))
        print(
            f"Balance after adding transactions: ${self.daniel.get_balance()}")
        self.assertEqual(self.daniel.get_balance(), 4950)

    def test_view_transactions(self):
        self.daniel.add_transaction(Income(100, "Gift", "Gifts"))
        transactions = self.daniel.view_transactions()
        print("\nList of transactions:")
        for transaction in transactions:
            print(transaction)
        self.assertIn(Income(100, "Gift", "Gifts"), transactions)

    def test_summary(self):
        self.daniel.add_transaction(Income(5000, "Monthly Salary", "Salary"))
        self.daniel.add_transaction(Expense(50, "Lunch", "Food"))
        summary = self.daniel.summary()
        print("\nSummary after adding transactions:")
        for key, value in summary.items():
            print(f"{key}: ${value}")
        self.assertEqual(summary['Total Income'], 5000)
        self.assertEqual(summary['Total Expense'], 50)
        self.assertEqual(summary['Balance'], 4950)


if __name__ == "__main__":
    unittest.main()
