import requests
import pprint

def test_v1_account():
    # Регистрация пользователя

    login = 'nm_test'
    email = 'nmtest@gmail.com'
    password = '12345678'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)

    # Получить письмо из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)

    # Получить активационный токен
    #Todo напишем логику позже

    # Активация пользователя

    headers = {
        'accept': 'text/plain',
    }

    response = requests.put('http://5.63.153.31:5051/v1/account/4670bb6c-ad97-4d15-a795-bf5e04acbd86', headers=headers)

    print(response.status_code)
    print(response.text)

# Авторизоваться
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)

    print(response.status_code)
    print(response.text)

