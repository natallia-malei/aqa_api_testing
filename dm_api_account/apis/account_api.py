from json import loads

import requests

from restclient.client import RestClient


class AccountApi(RestClient):
    # def __init__(
    #         self,
    #         host,
    #         headers=None
    # ):
    #     self.host = host
    #     self.headers = headers

    def post_v1_account(
            self,
            json_data
    ):
        """
        Register new user
        :param json_data:
        :return:
        """
        # вместо библиотеки request используем RestClient он использует собственные логируемые методы, поэтому self
        response = self.post(
            #url=f'{self.host}/v1/account',
            path=f"/v1/account",
            json=json_data
        )
        return response


    def put_v1_account_token(
            self,
            token
    ):
        """
        Activate registered user
        :param token:
        :return:
        """

        headers = {
            'accept': 'text/plain',
        }
        # response = requests.put
        response = self.put(
            #url=f'{self.host}/v1/account/{token}',
            path=f'/v1/account/{token}',
            headers=headers
        )
        return response

    def put_v1_account_email(
            self,
            json_data
        ):
        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }
        # response = requests.put
        response = self.put(
            #url = f'{self.host}/v1/account/email',
            path = f'/v1/account/email',
            headers=headers,
            json=json_data)
        return response