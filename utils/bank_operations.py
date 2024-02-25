import json
from function import transaction_filter

from model.transaction import Transaction

with open('../operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

transactions = []

"""
Распарсил данные JSON в список объектов Transaction
"""
for operation_data in data:
    transaction = Transaction(operation_data["id"],
                              operation_data["date"],
                              operation_data["state"],
                              operation_data["operationAmount"]["amount"] + " " +
                              operation_data["operationAmount"]["currency"]["name"],
                              operation_data["description"],
                              operation_data.get("from"),
                              operation_data.get("to")
                              )
    transactions.append(transaction)

last_executed_operations = transaction_filter(transactions)

for transaction in last_executed_operations:
    print(transaction)
    print('-' * 100)