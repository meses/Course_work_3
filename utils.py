import json
def read_file():
    with open('operations.json', 'r', encoding='UTF-8') as f:
        transactions_list = json.load(f)
    return transactions_list

#print(read_file()[0])
elem = read_file()

    #element = read_file()[0]
    #print(i.get('state'))
print(f'Всего элементов {len(elem)}')

transaction_list = read_file()
def sort_by_id(transaction_list:list):
    transaction_list_sorted = []
    transaction_list_sorted = transaction_list.sort(key=lambda d: d['date'], reverse=True)
    return transaction_list

#print(sort_by_id(read_file()))

def execute_transactios(transaction_list, sort_key, filter_key):
    """
    Сортирует и фильтрует список
    :param transaction_list: Исходный список
    :param sort_key: Ключ по которому сортирвоать
    :return: Фильтрованный и сортированный список
    """
    execute_list = []
    for i in transaction_list:
        if i.get('state') == filter_key:
            execute_list.append(i)
    execute_list.sort(key=lambda dictionary: dictionary[sort_key], reverse=True)
    return execute_list

#print(f'Элементов EXECUTED {len(execute_transactios(transaction_list))}')
for i in execute_transactios(transaction_list, 'date', 'EXECUTED'):
    print(i)

'''
def get_key(transaction_list):
    return transaction_list['date']

#filtered_list.sort(key=get_key(filtered_list))
#print(filtered_list)
filtered_list.sort(key=lambda dictionary: dictionary['date'], reverse=True)
for i in filtered_list:
    print(i)
'''