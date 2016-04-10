from phone2address import cli
import requests
import openpyxl

with open('tests/correct_response.html', 'r', encoding='gbk') as f:
    corrent_data = f.readlines()
    f.close()

with open('tests/wrong_response.html', 'r') as f:
    wrong_data = f.readlines()
    f.close()

response = requests.Response


def mock_request_get(url):
    base = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile='
    if url == base + '13012345678':
        response.text = str(corrent_data)
        return response
    else:
        response.text = str(wrong_data)
        return response


def read_from_file(source):
    from itertools import chain
    tmp = list(chain.from_iterable([i for i in source]))
    data = []
    for i in tmp:
        if i.value is not None:
            data.append(str(i.value))
    return data


def test_get_address(monkeypatch):
    monkeypatch.setattr('requests.get', mock_request_get)
    assert cli.get_address('13012345678') == ['重庆', '']
    assert cli.get_address('110') == False


def test_process_xlsx(monkeypatch):
    monkeypatch.setattr('requests.get', mock_request_get)
    cli.process('tests/test_xlsx.xlsx')
    source = openpyxl.load_workbook('tests/test_processed.xlsx').active
    target = openpyxl.load_workbook('tests/processed.xlsx').active
    assert read_from_file(source) == read_from_file(target)
