import re
from datetime import datetime


def transaction_filter(transactions):
    """
    Функция фильтрации операций
    Отфильтровал только те операции которые прошли успешно
    """
    executed_transactions = [transaction for transaction in transactions if transaction.state == "EXECUTED"]
    sorted_transactions = sorted(executed_transactions, key=lambda x: datetime.strptime(x.date, "%Y-%m-%dT%H:%M:%S.%f"),
                                 reverse=True)

    last_executed_operations = sorted_transactions[:5]

    return last_executed_operations


def account_format(account):
    """
    Функция, которая форматирует счет или карту отправителя
    :return:
    """
    search_account_name = re.findall(r'[a-zA-Zа-яА-Я]+', account)
    account_name = ''.join(search_account_name)
    account_name = re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', account_name)
    search_account_number = re.search(r"\d+", account).group()
    account_number = ''.join(search_account_number)

    if account_name == "Счет":
        formatted_account_number = account_name + " " + "**" + account_number[-4:]
        return formatted_account_number
    else:
        formatted_account_number = (account_name + " " + search_account_number[:4] + " " +
                                    search_account_number[4:6] + "** **** " + search_account_number[-4:])
        return formatted_account_number
