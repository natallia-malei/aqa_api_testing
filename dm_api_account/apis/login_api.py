import requests

from restclient.client import RestClient


class LoginApi(RestClient):
    # def __init__(
    #         self,
    #         host,
    #         headers=None
    # ):
    #     self.host = host
    #     self.headers = headers

    def post_v1_account_login(
            self,
            json_data,
    ):
        """
        Authenticate via credentials
        :param json_data:
        :return:
        """
        #response = requests.post
        response = self.post(
            # url=f'{self.host}/v1/account/login',
            path=f'/v1/account/login',
            json=json_data
        )
        return response
