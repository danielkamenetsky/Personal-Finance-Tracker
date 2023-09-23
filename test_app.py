import unittest
from app import User, Income, Expense, System


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def test_register_user(self):
        user = self.system.register("danielkamenetsky", "securepassword")
        self.assertIsInstance(user, User)

    def test_register_duplicate_username(self):
        self.system.register("danielkamenetsky", "securepassword")
        duplicate_user = self.system.register(
            "danielkamenetsky", "anotherpassword")
        self.assertIsNone(duplicate_user)

    def test_login_correct_credentials(self):
        self.system.register("danielkamenetsky", "securepassword")
        logged_in_user = self.system.login(
            "danielkamenetsky", "securepassword")
        self.assertIsInstance(logged_in_user, User)

    def test_login_incorrect_credentials(self):
        self.system.register("danielkamenetsky", "securepassword")
        wrong_user = self.system.login("danielkamenetsky", "wrongpassword")
        self.assertIsNone(wrong_user)

    def test_login_nonexistent_user(self):
        non_existing_user = self.system.login(
            "nonexistentuser", "somepassword")
        self.assertIsNone(non_existing_user)


class TestPersonalFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.daniel = User("danielkamenetsky", "securepassword")

    def test_add_transaction(self):
        self.daniel.add_transaction(Income(5000, "Monthly Salary", "Salary"))
        self.daniel.add_transaction(Expense(50, "Lunch", "Food"))
        self.assertEqual(self.daniel.get_balance(), 4950)

    def test_view_transactions(self):
        self.daniel.add_transaction(Income(100, "Gift", "Gifts"))
        transactions = self.daniel.view_transactions()
        self.assertIn(Income(100, "Gift", "Gifts"), transactions)

    def test_summary(self):
        self.daniel.add_transaction(Income(5000, "Monthly Salary", "Salary"))
        self.daniel.add_transaction(Expense(50, "Lunch", "Food"))
        summary = self.daniel.summary()
        self.assertEqual(summary['Total Income'], 5000)
        self.assertEqual(summary['Total Expense'], 50)
        self.assertEqual(summary['Balance'], 4950)


if __name__ == "__main__":
    unittest.main()
