import json
from pathlib import Path 

from models.expense import Expense


EXPENSES_FILE = Path(__file__).parent.parent.parent / 'data' / 'expenses.json'

def write_json(expenses):
    try:
        EXPENSES_FILE.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f'Permission denied: Unable to create directory {EXPENSES_FILE.parent}.')
        return
    except Exception as e:
        print(f'An error occurred while creating directory {EXPENSES_FILE.parent}: {e}')
        return

    try:
        list_expenses = [expense.to_dict() for expense in expenses]
    except AttributeError:
        print('Error: One or more items in the expenses list do not have a to_dict() method.')
        return

    try:
        with open (EXPENSES_FILE, 'w', encoding='utf8') as f: 
            json.dump(list_expenses, f, indent=2) 
    except PermissionError:
        print(f'Permission denied: Unable to write to file {EXPENSES_FILE}.')
    except Exception as e:
        print(f'An error occurred while writing to file {EXPENSES_FILE}: {e}')

def read_json():
    try:
        with open(EXPENSES_FILE, 'r', encoding='utf8') as f:
            file_data = json.load(f)

    except FileNotFoundError:
        print(f'File not found: {EXPENSES_FILE}. Returning an empty list.')
        return []
    except PermissionError:
        print(f'Permission denied: Unable to read file {EXPENSES_FILE}. Returning an empty list.')
        return []
    except json.JSONDecodeError:
        print(f'Error decoding JSON from file {EXPENSES_FILE}. Returning an empty list.')
        return []
    except Exception as e:
        print(f'An unexpected error occurred while reading file {EXPENSES_FILE}: {e}. Returning an empty list.')
        return []

    if not isinstance(file_data, list):
        print(f'Unexpected data format in file {EXPENSES_FILE}. Expected a list. Returning an empty list.')
        return []
    
    expenses = []
    for index, item in enumerate(file_data, start=1):
        if not isinstance(item, dict):
            print(f'Unexpected item format at index {index} in file {EXPENSES_FILE}. Expected a dictionary. skipping this item.')
            continue

        try:
            expense = Expense(**item)
            expenses.append(expense)

        except TypeError as e:
            print(f'Error creating Expense object from item at index {index} in file {EXPENSES_FILE}: {e}. Skipping this item.')
        except KeyError as e:
            print(f'Missing excpected key {e} in item at index {index} in file {EXPENSES_FILE}. Skipping this item.')
        except Exception as e:
            print(f'An unexpected error occurred while processing item at index {index} in file {EXPENSES_FILE}: {e}. Skipping this item.')

    return expenses



    # with open('archive.json', 'r',) as f: # json.load(archive.json)