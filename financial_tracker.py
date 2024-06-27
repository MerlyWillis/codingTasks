# Financial Tracker.

income_tracker = {}
expense_tracker = {}

def add_income(income_source, income_figure):
    income_tracker[income_source] = income_figure
    print('Income source & figure successfully added to database.')
    
def add_expense(expense_place, expense_figure):
    expense_tracker[expense_place] = expense_figure
    print('Expense source & figure successfully added to database.')

def display_disposable():
    total_income = 0
    total_expense = 0
    for val in income_tracker.values():
        total_income += val
    for exp in expense_tracker.values():
        total_expense += exp
    total_disposable = (total_income - total_expense)
    print(f'Total disposable income per month is £{total_disposable}')
    
def display_salary():
    salary = 0
    for x in income_tracker.values():
        salary += x
    print(f'Total salary is £{salary}')
    
def display_expense():
    expense = 0
    for x in expense_tracker.values():
        expense += x
    print(f'Total expense is £{expense}')
    
def display_hierarchy():
    print('Income sources from highest to lowest...')
    incomes_sorted = sorted(income_tracker.items(), key=lambda x: x[1], reverse=True)
    for key, value in incomes_sorted:
        print(f'{key}: £{value}')
    print('Places of expense from highest to lowest...')
    expenses_sorted = sorted(expense_tracker.items(), key=lambda x: x[1], reverse=True)
    for key, value in expenses_sorted:
        print(f'{key}: £{value}')
        
def budget_tracker():
    if not bool(income_tracker) or not bool(expense_tracker):
        print('Can\'t perform task income/expense data not provided.')
    else:
        total_income = 0
        total_expense = 0
        for val in income_tracker.values():
            total_income += val
        for exp in expense_tracker.values():
            total_expense += exp
        income_target = int(input('Enter income target: '))
        expense_budget = int(input('Enter expense budget: '))
        income_percentage = (total_income / income_target) * 100
        expense_percentage = (total_expense / expense_budget) * 100
        print('Incomes Breakdown: ')
        print(f'{round(income_percentage)}%')
        if 0 <= round(income_percentage) <= 50:
            print('Less than 50% of your budget, increase your income.')
        elif 50 < round(income_percentage) <= 85:
            print('You\'re over 50% of your budget, well done.')
        elif 85 < round(income_percentage) <= 100:
            print('You\'re over 85% your income target, keep going.')
        else:
            print('You\'re exceeding 100% of your target, congratulations.')
        
        print('Expenses Breakdown: ')
        print(f'{round(expense_percentage)}%')
        if 0 <= round(expense_percentage) <= 50:
            print('You\'re below 50% of your budget, well done.')
        elif 50 < round(expense_percentage) <= 85:
            print('You\'re over 50% of your budget, watch your spending.')
        elif 85 < round(expense_percentage) <= 100:
            print('You\'re exceeding 85% of your budget, cut down your spending.')
        else:
            print('You\'re exceeding 100% of your expense budget, you have failed.')
    
    
    
print('Welcome to the financial tracker tool.')
    
while True:
    print('Please make a choice from the list below.')
    print('1. Add Income Source & Figure.')
    print('2. Add Expense Place & Figure.')
    print('3. Display Monthly Disposable Balance.')
    print('4. Display Income Summary.')
    print('5. Display Expense Summary.')
    print('6. Display Hierarchy of Incomes & Expenses.')
    print('7. Budget Tracker.')
    print('8. Exit.')
    choice = input('Enter Choice: ')
    
    if choice == '1':
        income_source = input('Enter source of income: ')
        income_figure = int(input('Enter income figure: '))
        add_income(income_source, income_figure)
    elif choice == '2':
        expense_place = input('Enter place of expense: ')
        expense_figure = int(input('Enter figure of expense: '))
        add_expense(expense_place, expense_figure)
    elif choice == '3':
        display_disposable()
    elif choice == '4':
        display_salary()
    elif choice == '5':
        display_expense()
    elif choice == '6':
        display_hierarchy()
    elif choice == '7':
        budget_tracker()
    elif choice == '8':
        print('Thanks for using the financial tracker tool.')
        break
    else:
        print('Invalid entry, please make a choice (1-8)')
    