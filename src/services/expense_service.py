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
    print('\n--- What do you want to edit? ---')
    print('1 - Store name')
    print('2 - Amount')
    print('3 - Category')
    print('4 - Payment method')
    print('5 - Release Date')
    print('6 - Everything')
    print('0 - Cancel')

    while True:
        option = ui.inputs.get_int('Choice an option: ')

        if 0 <= option <= 6:
            return option
        
        print('\nInvalid option. Please try again.\n')

def get_current_value(expense, attribute):
    value = getattr(expense, attribute, 'N/A')
    if hasattr(expense, 'format_field'):
        return expense.format_field(attribute, value)
    return value

def get_new_value(expense, attribute):
    current_value = get_current_value(expense, attribute)

    print(f'\nCurrent {attribute.replace("_", " ")}: {current_value}')

    if attribute == 'store_name':
        return ui.inputs.get_name('New store name: ')

    if attribute == 'amount':
        return ui.inputs.read_float('New amount: ')

    if attribute == 'category':
        return input ('New category: ').strip()

    if attribute == 'payment_method':
        return input('New payment method: ').strip()

    if attribute == 'release_date':
        return ui.inputs.get_date('New release date: ')

def collect_expense_updates(expense, option):
    fields = {
        1: 'store_name',
        2: 'amount',
        3: 'category',
        4: 'payment_method',
        5: 'release_date'
    }

    if option == 6:
        selected_fields = list(fields.values())
    else:
        selected_fields = [fields[option]]

    updates = {}

    for attribute in selected_fields:
        new_value = get_new_value(expense, attribute)
        updates[attribute] = new_value

    return updates

def show_changes(expense, updates):
    print('\n--- Review Changes ---')

    for attribute, new_value in updates.items():
        old_value = getattr(expense, attribute, 'N/A')

        old_display = expense.format_field(
            attribute,
            old_value
        )

        new_display = expense.format_field(
            attribute,
            new_value
        )

        field_name = attribute.replace('_', ' ').title()

        print(f'\n{field_name}')
        print(f'    Current : {old_display}')
        print(f'    New     : {new_display}')


    print('\n' + '-' * 40)

def confirm_changes():
    while True:
        answer = input('\nSave these changes? (Y/N): ').strip().lower()

        if answer in ('y', 'yes'):
            return True

        if answer in ('n', 'no'):
            return False

        print('Please enter Y or N')

def apply_expense_updates(expense, updates):
    for attribute, value in updates.items():
        setattr(expense, attribute, value)

def update_expense():
    expenses = read_json()

    if not expenses:
        print('\nNo expenses found.')
        return
    
    list_expenses()

    while True:
        index = ui.inputs.get_int(
            '\nWhich expense do you want to edit? '
            )

        if 1 <= index <= len(expenses):
            break

        print('\nInvalid expense number. '
        f'Please choose a number between 1 and {len(expenses)}.'
        )
    
    expense = expenses[index - 1]

    print(f'\n---Selected Expense #{index} ---')
    print(expense)
    print('-' * 40)

    option = get_field_to_edit()

    if option == 0:
        print('\nOperation cancelled.')
        return

    updates = collect_expense_updates(expense, option)

    if not updates:
        print('\nNo changes were made.')
        return

    show_changes(expense, updates)

    if not confirm_changes():
        print('\nOperation cancelled. No changes were saved.')
        return

    apply_expense_updates(expense, updates)
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
            print('\nInvalid expense number.')
            continue

        expenses.pop(index - 1)
        write_json(expenses)
        print('Expense deleted successfully!')
        break

