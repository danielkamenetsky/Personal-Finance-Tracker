import unittest
from app import User, Income, Expense  # assuming app.py contains these classes


class TestPersonalFinanceTracker(unittest.TestCase):

    def setUp(self):
        # Setup code: This runs before every test
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
