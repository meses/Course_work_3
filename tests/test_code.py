from utils import read_file, execute_transactios, hide_symbols_account, transfom_date_fomat


def test_read_file():
    assert type(read_file('operations.json')) == list

def test_execute_transactios():
    transaction_list = read_file('operations.json')
    assert type(execute_transactios(transaction_list, 'date', 'EXECUTED')) == list

def test_hide_symbols_account():
    assert hide_symbols_account('Счет 64686473678894779589') == 'Счет **9589'
    assert hide_symbols_account('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert hide_symbols_account('Visa Platinum 8990922113665229') == 'Visa Platinum 8990 92** **** 5229'

def test_transfom_date_fomat():
    assert transfom_date_fomat('2019-08-26') == '26.08.2019'
    assert transfom_date_fomat('2019-08-26T10:50:58.294041') == '26.08.2019'

