"""Test functions for Expense module"""

from expense import Expense

expense = Expense()
expense.add('12/01/20', 'Groceries', 'Vons', 25, 'Credit Card')
expense.add('12/01/20', 'Rent', 'December Rent', 1000, 'Check')
expense.add('12/01/20', 'School', 'Tuition', 4000, 'Check')


def test_initialize():
    assert isinstance(expense, Expense)
    assert isinstance(expense.expense_list, list)


def test_add():
    entry_1 = expense.expense_list[0]
    assert isinstance(entry_1, dict)
    assert entry_1 == {
        'Date': '12/01/20', 'Category': 'Groceries', 'Description': 'Vons',
        'Amount': 25, 'Form': 'Credit Card'}


def test_total():
    total = expense.total()
    assert total == 5025


def test_max():
    most_expensive = expense.highest()
    assert most_expensive == 4000
