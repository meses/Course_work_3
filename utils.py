import json
def read_file():
    with open('operations.json', 'r', encoding='UTF-8') as f:
        transactions_list = json.load(f)
    return transactions_list


def execute_transactios(transaction_list, sort_key, filter_key):
    """
    Сортирует и фильтрует список
    :param transaction_list: Исходный список
    :param sort_key: Ключ по которому сортирвоать список
    :param filter_key: Ключ по которому фильтровать список
    :return: Фильтрованный и сортированный список
    """
    execute_list = []
    for i in transaction_list:
        if i.get('state') == filter_key:
            execute_list.append(i)
    execute_list.sort(key=lambda dictionary: dictionary[sort_key], reverse=True)
    return execute_list


def hide_symbols_account(bank_account:str):
    """
    Маскирует номер счёта или карты
    :param bank_account: Тип и номер
    :return: Маскированный тип и номер
    """
    if bank_account.split(' ')[0] == 'Счет':
        account_number = bank_account.split(' ')[1]
        account_name = bank_account.split(' ')[0]
        hyde_account_number = "**"+account_number[-4:len(account_number)]
        hyde_bank_account_list = []
        hyde_bank_account_list.append(account_name)
        hyde_bank_account_list.append(hyde_account_number)
        hyde_bank_account = ' '.join(hyde_bank_account_list)
    else:
        account_number = bank_account.split(' ')[-1]
        account_name = bank_account.split(' ')[:-1]
        account_number_hyde = account_number[:6] + "******" + account_number[12:16]
        account_number_hyde_sep = ' '.join([account_number_hyde[i:i+4] for i in range(0, len(account_number_hyde), 4)])
        hyde_bank_account_list = []
        hyde_bank_account_list.append(' '.join(account_name))
        hyde_bank_account_list.append(account_number_hyde_sep)
        hyde_bank_account = ' '.join(hyde_bank_account_list)
    return hyde_bank_account

def transfom_date_fomat(original_date:str):
    """
    Преобразует формат даты с ГГГ-ММ-ДД в ДД.ММ.ГГГГ
    :param original_date: Строка в формате ГГГ-ММ-ДД
    :return: Строка в формате ДД.ММ.ГГГГ
    """
    date_str = original_date.split('T')[0]
    date_list = date_str.split('-')
    date_list.reverse()
    transformed_date = '.'.join(date_list)
    return transformed_date