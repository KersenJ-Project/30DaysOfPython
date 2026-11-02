

class PersonAccount():
    def __init__(self, firstname = None, lastname = None, incomes = None, expenses = None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses  = expenses

    def total_income(self):
        print("Total income: ", sum(self.incomes))

    def total_expense(self):
        print("Total expenses: ", sum(self.expenses))

    def account_info(self):
        print(f"Hello {self.firstname} {self.lastname}. Incomes: {self.incomes}, Expenses: {self.expenses}")

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def account_balance(self):
        return sum(self.incomes) - sum(self.expenses) 

def main():
    # Create a person account
    account = PersonAccount("John", "Doe")

    # Add incomes
    account.add_income(2500)
    account.add_income(1500)
    account.add_income(500)

    # Add expenses
    account.add_expense(800)
    account.add_expense(300)
    account.add_expense(200)

    # Display account information
    account.account_info()

    # Display total income
    account.total_income()

    # Display total expenses
    account.total_expense()

    # Display account balance
    print("Account balance: ", account.account_balance())


if __name__ == "__main__":
    main()