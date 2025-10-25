import requests
import pprint
from json import loads

def test_v1_account():
    # Регистрация пользователя

    login = 'nm_test2'
    email = 'nmtest2@gmail.com'
    password = '12345679'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'
    #проверь если в нашем объекте статус код не 201 тогда выведи сообщение

    # Получить письмо из почтового сервера
    params = {
        'limit': '50',
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Письма не были получены'

    # Получить активационный токен
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body']) #чтобы получить логин и токен
        user_login = user_data['Login']
        if user_login == login:
            print(user_login)
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            print(token)

    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активация пользователя
    headers = {
        'accept': 'text/plain',
    }

    response = requests.put(f'http://5.63.153.31:5051/v1/account/{token}', headers=headers)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Пользователь не был активирован'

    # Авторизоваться
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Пользователь не смог авторизоваться'

