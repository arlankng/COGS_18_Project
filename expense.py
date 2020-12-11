"""Expense tracker that requires the date, category, description, amount, and
form of payment"""

import matplotlib.pyplot as plt
from random import randint


class Expense():
    """Class to create Expense objects."""

    def __init__(self):
        """Expense_list initializer."""

        # Self.expense_list is always an empty list when called
        self.expense_list = []

    def add(self, date, category, description, amount, form):
        """Adds information about a new expense to the expense list.

        Parameters
        ----------
        date: string
            The date of the expense.
        category: string
            The category of the expense.
        description: string
            A short description about the expense.
        amount: int or float
            The amount of the expense.
        form: string
            The form of payment of the expense.
        """

        # Creates the dictionary
        dict_expense = {
            'Date': date, 'Category': category, 'Description': description,
            'Amount': amount, 'Form': form}

        # Appendds the dictionary to self.expense_list
        self.expense_list.append(dict_expense)

        # Raises an error is the amount is not an int or float.
        if not isinstance(dict_expense['Amount'], (int, float)):
            raise TypeError('Input amount must be a number')

    def total(self):
        """Totals up all the expense in the expense list.

        Returns
        -------
        total: int or float
            The total sum of all the amounts
        """

        total = 0

        # Iterates through the expense list to add to the total.
        for i in self.expense_list:
            # Updates the total amount
            total = total + i['Amount']
        return total

    def highest(self):
        """Most expensive expense in the expense list.

        Returns
        -------
        highest: int or float
            The max value of all the amounts
        """

        # Creates a list of all the amounts and finds the max of them all.
        highest = max(i['Amount'] for i in self.expense_list)
        return highest

    def print_expense(self):
        """Prints out each item in the expense list.

        Returns
        -------
        self.expense_list: list of dictionaries
        """

        # Iterates through self.expense_list to print each item on a new line
        for i in self.expense_list:
            print(i)

    def sort_by(self, variable):
        """Sorts the expense list by a given variable and then prints the
        expense list.

        Returns
        -------
        sorted_list: list of dictionaries
            Expense list sorted by the given variable
        """

        # Sorts the expense list by the given variable.
        sorted_list = sorted(self.expense_list, key=lambda i: i[variable])

        # Prints the expense list
        for i in sorted_list:
            print(i)

    def spent_on(self, date):
        """Prints out list of expenses on a given date.

        Returns
        -------
        spent_list: list of dictionaries
            All expenses that match the given date
        """

        # Searches through the expense list that matches the given date.
        spent_list = [i for i in self.expense_list if i['Date'] == date]

        # Prints the given date list.
        for i in spent_list:
            print(i)

    def plot_by(self, variable):
        """Represents all expenses as a pie chart based on a given variable.

        Parameters
        ----------
        variable: string
            The key that the pie chart will be based on.
        """

        # The variable and amount used for the pie chart.
        keys = (variable, 'Amount')

        # Isolates the variable and amount that will be used.
        new_list = [{k: i[k] for k in keys} for i in self.expense_list]
        # Creates a new list with the variable as the key and amount as the
        # item.
        updated_list = [{i[variable]: i['Amount']} for i in new_list]

        # Creates a new dictionary that consolidates any duplicate key
        plot_list = {}
        for dict in updated_list:
            for list in dict:
                if list in plot_list:
                    # Adds new amount to the existing amount if duplicate.
                    plot_list[list] += (dict[list])
                else:
                    # Adds new key and item to dictionary if not in it.
                    plot_list[list] = dict[list]

        # Creates a tuple of the labels
        labels = tuple([i for i in plot_list])
        # Creates a list of the size of each category
        sizes = [plot_list[i] for i in plot_list]

        # Creates the pie chart
        fig, ax = plt.subplots()
        explode = tuple(randint(0, 1) * 0.1 for i in range(len(sizes)))
        ax.pie(sizes, explode=explode, labels=None, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.legend(labels, loc="best")
        ax.axis('equal')
        plt.title('Expense List based on ' + variable + "\n")
        plt.tight_layout()
        plt.show()
