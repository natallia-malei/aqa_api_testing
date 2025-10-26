from json import loads

from api_mailhoog.apis.mailhog_api import MailhogApi
from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi


def test_put_v1_account_email():
    # Регистрируемся
    account_api = AccountApi(host='http://5.63.153.31:5051')
    login_api = LoginApi(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi(host='http://5.63.153.31:5025')

    login = 'nm_test13'
    email = f'{login}@gmail.com'
    password = '12345679'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'
    # проверь если в нашем объекте статус код не 201 тогда выведи сообщение

    # Получить письмо из почтового сервера
    response = mailhog_api.get_api_v2_messages()
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Письма не были получены'

    # Получаем активационный токен
    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активируем
    response = account_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Пользователь не был активирован'

    # Заходим
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Пользователь не смог авторизоваться'

    # Меняем емейл
    new_email = f'{login}_new@gmail.com'

    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': token,
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': login,
        'password': password,
        'email': new_email,
    }

    response = requests.put('http://5.63.153.31:5051/v1/account/email', headers=headers, json=json_data)
    assert response.status_code == 200, 'Не удалось сменить email'

    # Пытаемся войти, получаем 403
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }
    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code, response.text)
    assert response.status_code == 403, 'В доступе отказано, проверьте email'

    # На почте находим токен по новому емейлу для подтверждения смены
    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, 'Письма не были получены'

    # Извлекаем токен подтверждения смены email
    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активируем этот токен
    response = account_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, 'Пользователь не был активирован'

    # Логинимся
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }
    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code, response.text)
    assert response.status_code == 200, 'Не удалось авторизоваться с новым email'


def get_activation_token_by_login(
        login,
        response
    ):
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])  # чтобы получить логин и токен
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
    return token
