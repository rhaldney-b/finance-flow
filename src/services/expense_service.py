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

def update_expense():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return
    list_expenses()

    while True:
        index = ui.inputs.get_int('\nWhich expense do you want to edit? ')

        if not 1 <= index <= len(expenses):
            print('\n Invalid expense number.')
            continue
    
        expense = expenses[index - 1]
        break
        


    print('\nWhat do you want to edit?')
    print('1 - Store name')
    print('2 - Amount')
    print('3 - Category')
    print('4 - Payment method')
    print('5 - Release Date')
    print('6 - Everything')

    option = ui.inputs.get_int('Choice an option: ')
    if option == '1':
        expense.store_name = ui.inputs.get_name('Name: ')

    elif option == '2':
        expense.amount = ui.inputs.read_float('Amount: ')

    elif option == '3':
        expense.category = input('New category: ')

    elif option == '4':
        expense.payment_method = input('New payment method: ')

    elif option == '5':
        expense.release_date = ui.inputs.get_date('Release date: ')
        
    elif option == '6':
        expense.store_name = ui.inputs.get_name('Name: ')
        expense.amount = ui.inputs.read_float('Amount: ')
        expense.category = input('New category: ')
        expense.payment_method = input('New payment method: ')
        expense.release_date = ui.inputs.get_date('Release date: ')
    else:
        print('Option not exists.')
        return

    write_json(expenses)
    print('Expense updated sucessfully!')

def delete_expense():
    expenses = read_json()

    if not expenses:
        print('\nNo expenses found.')
        return

    list_expenses()

    while True:
        index = ui.inputs.get_int(
            '\nWhich expense do you want to delete? '
        )

        if not 1 <= index <= len(expenses):
            print('\nInvalid expenser number.')
            continue

        expenses.pop(index - 1)
        write_json(expenses)
        print('Expense deleted successfully!')
        break