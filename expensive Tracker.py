# 1. create a add function to add expenses

def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# 2. create a function to print expenses

def print_expeneses(expenses):
    for expense in expenses:
        print(f'amount: {expense["amount"]}, category: {expense["category"]} ')

# 3. create a funtion to desplay total expanses

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# 4. create a funtion to filter expenses by category

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# 5. create a funtion to run the program
def main():
    expenses = []
    while True:
        print('\n------Expense tracker------')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount spent: '))
            category = input('Enter a category (Entertainment, Food, Health, Bills, Etc): ')
            add_expenses(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses: ')
            print_expeneses(expenses)
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}: ')
            expenses_for_category = filter_expenses_by_category(expenses, category)
            print_expeneses(expenses_for_category)
        elif choice == '5':
            print('Exiting the program.')
            break

main()

