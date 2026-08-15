from models.expense import Expense
from services.storage import write_json, read_json
import ui.inputs

def add_expense(last_date=None):
    store_name = ui.inputs.get_name('Name: ')
    amount = ui.inputs.read_float('Amount: ')
    category = input('Category: ')
    payment_method = input('Payment method: ')
    release_date = ui.inputs.get_date('Release date: ', default_date=last_date)
    return Expense(store_name, amount, category, payment_method, release_date)

def save_expense():
    last_date = None
    while True:
        expense = add_expense(last_date)
        last_date = expense.release_date
        write_json(read_json() + [expense])
        choice = input('Add another expense? [Y/N]: ').strip().lower()
        if choice == 'n':
            break

def list_expenses():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return

    print('Expenses: ')
    for index, expense in enumerate(expenses, start = 1):
        print('=' * 40)
        print(f'{index}. {expense}')
    return 


def get_field_to_edit():
    print('\nWhat do you want to edit?')
    print('1 - Store name')
    print('2 - Amount')
    print('3 - Category')
    print('4 - Payment method')
    print('5 - Release Date')
    print('6 - Everything')

    while True:
        option = ui.inputs.get_int('Choice an option: ')
        if 1 <= option <= 6:
            return option
        print('\nInvalid option. Please try again.\n')    

def apply_expense_updates(expense, option):
    if option in (1, 6):
        expense.store_name = ui.inputs.get_name('Name: ')
    if option in (2, 6):
        expense.amount = ui.inputs.read_float('Amount: ')
    if option in (3, 6):
        expense.category = input('New category: ')
    if option in (4, 6):
        expense.payment_method = input('New payment method: ')
    if option in (5, 6):
        expense.release_date = ui.inputs.get_date('Release date: ')


def update_expense():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return
    
    list_expenses()

    while True:
        index = ui.inputs.get_int('\nWhich expense do you want to edit? ')

        if 1 <= index <= len(expenses):
            break
        print('\nInvalid expense number.')
    
    expense = expenses[index - 1]

    option = get_field_to_edit()
    apply_expense_updates(expense, option)

    write_json(expenses)
    print('Expense updated sucessfully!')

def delete_expense():
    expenses = read_json()

    if not expenses:
        print('\nNo expenses found.')
        return

    list_expenses()

    while True:
        index = ui.inputs.get_int('Which expense do you want to delete? ')

        if not 1 <= index <= len(expenses):
            print('\nInvalid expenser number.')
            continue

        expenses.pop(index - 1)
        write_json(expenses)
        print('Expense deleted successfully!')
        break

