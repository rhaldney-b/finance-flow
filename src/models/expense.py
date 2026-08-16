from datetime import datetime, date
import locale


class Expense:
    def __init__(self, store_name, amount, category, payment_method, release_date):
        self.store_name = store_name
        self.amount = amount
        self.category = category
        self.payment_method =  payment_method
        self.release_date = self._parse_date(release_date)

    def _parse_date(self, date_value):
        if isinstance(date_value, (datetime, date)):
            return date_value
        if isinstance(date_value, str):
            for fmt in ('%Y-%m-%d', '%d/%m/%Y', 'Y-%m-%d %H:%M:%S'):
                try:
                    return datetime.strptime(date_value, fmt)
                except ValueError:
                    pass
            raise ValueError(f'Invalid date format: {date_value}')
        raise TypeError(f'Invalid date type: {type(date_value)}')

    @classmethod
    def from_dict(cls,data):
        return cls(**data)
    
    def __str__(self):
        try:
            amount_formatted = locale.currency(self.amount, grouping=True)
        except ValueError:
            amount_formatted = f'{self.amount:.2f}'

        date_formatted = self.release_date.strftime ('%d/%m/%Y')

        return (
            f'Store: {self.store_name}\n'
            f'Amount: {amount_formatted}\n'
            f'Category: {self.category}\n'
            f'Payment Method: {self.payment_method}\n'
            f'Realease Date: {date_formatted}\n'
        )

    def __repr__(self):
        return (
            f'Expense(store_name={self.store_name!r}, amount={self.amount},'
            f'category={self.category!r}, payment_method={self.payment_method!r}'
            f'release_date={self.release_date.strftime('%Y-%m-%d')!r})'
        )

    def to_dict(self):
        return {
        'store_name': self.store_name,
        'amount': self.amount,
        'category': self.category,
        'payment_method': self.payment_method,
        'release_date': self.release_date.strftime('%Y-%m-%d')
        }
