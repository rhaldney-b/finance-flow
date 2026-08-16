from datetime import datetime
import locale
import getpass

def configure_locale():
    USER = 'rhald'

    actual_user = getpass.getuser()

    if actual_user == USER:
        pt_locales = [
            'Portuguese_Brazil.1252',
            'Portuguese_Brazil',
            'pt-BR',
            'pt_BR.UTF-8',
            'pt_BR'
        ]

        for loc in pt_locales:
            try:
                locale.setlocale(locale.LC_ALL, loc)
                return loc
            except locale.Error:
                continue

    try:
        return locale.setlocale(locale.LC_ALL, '')
    except locale.Error:
        locale.setlocale(locale.LC_ALL, 'C')
        return 'C'

    configure_locale()


def read_float(prompt= ''):
    while True:
        raw_input = input(prompt).strip()

        clean_input = raw_input.replace(',', '.').replace(' ', '')

        try:
            amount = float(clean_input)
            if amount > 0:
                return amount
            else:
                print('Amount must be greater than zero.\n')
        except ValueError:
            print('Enter a valid number.\n')

def get_date(prompt='', default_date=None):
    while True:
        if default_date:
            display_prompt = f'ENTER FOR {default_date:%d/%m/%Y}: ' 
        else:
            display_prompt = prompt
        date = input(display_prompt).strip()
        if not date and default_date:
            return default_date
        try:
            date_strp = datetime.strptime(date, '%d/%m')
            return date_strp.replace(year=datetime.now().year)
        except ValueError:
            pass
        try:
            date_strp = datetime.strptime(date, '%d/%m/%Y')
            return date_strp
        except ValueError:
            print('Invalid date. Please use DD/MM or DD/MM/YYYY.\n')

def get_name(prompt= ''):
    while True:
        store_name = input(prompt).strip()
        if store_name:
            return store_name
        
        print('Name cannot be empty.\n')

def get_int(prompt=''):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('\nInvalid input. Please enter a valid integer.\n')
    


