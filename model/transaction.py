import re
from datetime import datetime
from utils.function import account_format


class Transaction:
    def __init__(self, transaction_id, date, state, operation_amount, description, from_account=None, to_account=None):
        self.id = transaction_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_account = from_account
        self.to_account = to_account

    def __str__(self):
        """
        Отформатировал дату по требованиям программы
        """
        date_obj = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_obj.strftime("%d.%m.%Y")

        if self.from_account is not None:
            formatted_card_number = account_format(self.from_account)
        else:
            formatted_card_number = "Открытие счета"

        if self.to_account is not None:
            formatted_account_number = account_format(self.to_account)
        else:
            formatted_account_number = "Открытие счета"

        return f"""
        {formatted_date} {self.description}
        {formatted_card_number} -> {formatted_account_number}
        {self.operation_amount}
        """