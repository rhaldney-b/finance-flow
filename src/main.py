from services import expense_service
from ui.menu import menu

if __name__ == '__main__':
        while True:
            choice = menu()

            if choice == '1':
                expense_service.save_expense()

            elif choice == '2':
                expense_service.list_expenses()

            elif choice == '3':
                expense_service.update_expense()

            elif choice == '4':
                expense_service.delete_expense()

            elif choice == '0':
                break