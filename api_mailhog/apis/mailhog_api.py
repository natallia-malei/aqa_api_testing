import requests

from restclient.client import RestClient
from restclient.configuration import Configuration


class MailhogApi(RestClient):
    # def __init__(
    #         self,
    #         host,
    #         headers=None
    # ):
    #     self.host = host
    #     self.headers = headers

    def __init__(
            self,
            configuration: Configuration
    ):
        super().__init__(configuration)
        self.mailhog_api = None

    def get_api_v2_messages(
            self,
            limit=50
    ):
        """
        Get users emails
        :return:
        """
        params = {
            'limit': limit,
        }
        # response = requests.get
        response = self.get(
            # url=f'{self.host}/api/v2/messages',
            path=f'/api/v2/messages',
            params=params,
            verify=False
        )
        return response
