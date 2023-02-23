from utils import read_file, execute_transactios, hide_symbols_account, transfom_date_fomat

transaction_list = read_file()
filtered_sorted_list = execute_transactios(transaction_list, 'date', 'EXECUTED')[:5]


for i in filtered_sorted_list:
    if 'from' in i.keys():
        print(transfom_date_fomat(i['date']), i['description'])
        print(f"{hide_symbols_account(i['from'])} -> {hide_symbols_account(i['to'])}")
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print('')

    else:
        print(transfom_date_fomat(i['date']), i['description'])
        print(hide_symbols_account(i['to']))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print('')
