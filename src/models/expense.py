from datetime import datetime
import locale


class Expense:
    def __init__(self, store_name, amount, category, payment_method, release_date):
        self.store_name = store_name
        self.amount = amount
        self.category = category
        self.payment_method =  payment_method
        self.release_date = release_date  

    def __str__(self):
        return f"""Store: {self.store_name}\nAmount: {locale.currency(self.amount, grouping=True)}\nCategory: {self.category}
Payment Method: {self.payment_method}
Realease Date: {self.release_date}"""

    def __repr__(self):
        return f"""Store: {self.store_name}\nAmount: {self.amount}\nCategory: {self.category}
Payment Method: {self.payment_method}
Realease Date: {self.release_date}"""

    def to_dict(self):
        return {
        'store_name': self.store_name,
        'amount': self.amount,
        'category': self.category,
        'payment_method': self.payment_method,
        'release_date': self.release_date.strftime('%Y-%m-%d') if hasattr(self.release_date, 'strftime') else self.release_date
        }
