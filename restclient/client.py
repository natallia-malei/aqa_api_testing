from requests import (
    session,
    JSONDecodeError,
)
import structlog
import uuid

class RestClient:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.log = structlog.getLogger(__name__).bind(service='api')

    def post(
            self,
            path,
            **kwargs
    ):
        return self._send_request(method='POST', path=path, **kwargs)

    def get(
            self,
            path,
            **kwargs
    ):
        return self._send_request(method='GET', path=path, **kwargs)


    def put(
            self,
            path,
            **kwargs
    ):
        return self._send_request(method='PUT', path=path, **kwargs)

    def delete(
            self,
            path,
            **kwargs
    ):
        return self._send_request(method='DELETE', path=path, **kwargs)

     # метод который логирует запросы
     # нужно подтянуть специальную библиотеку pip install structlog чтобы сделать логи читаемыми
    def _send_request(self, method, path, **kwargs):
        log = self.log.bind (event_id=str(uuid.uuid4())) # для получения по логам уникального id
        full_url = self.host + path

        log.msg(
            event='Request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data')
        )
        rest_response = self.session.request(method=method, url=full_url, **kwargs)

        log.msg(
            event='Response',
            status_code=rest_response.status_code,
            headers=rest_response.headers,
            json=self._get_json(rest_response),
        )
        return rest_response

   # тк json не возвращается в методе post пишем эту функцию
    @staticmethod #не использует функции и параметры внутри этого класса
    def _get_json(
            rest_response
    ):
        try:
            return rest_response.json()
        except JSONDecodeError:
            return {}






