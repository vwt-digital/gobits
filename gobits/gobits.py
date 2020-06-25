import os
import time


class Gobits:
    """
    A small class that holds information (bits) for a pub/sub message payload.

    Attributes:
        _data               A dictionary holding GCP trigger information.
        _request            An instance of werkzeug.local.LocalProxy.
        created             Date of creation in milliseconds since epoch (UTC).
        project             The source GCP project.
        function_name       Name of the processing cloud function.
        function_version    Version of the processing cloud function.
    """

    def __init__(self, data=None, request=None):
        self._data = data
        self._request = request
        self.created = str(int(round(time.time() * 1000)))
        self.project = os.getenv('X_GOOGLE_GCP_PROJECT')
        self.function_name = os.getenv('X_GOOGLE_FUNCTION_NAME')
        self.function_version = os.getenv('X_GOOGLE_FUNCTION_VERSION')

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        self._request = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def id(self):
        if self._request:
            return self._request.get('environ', {}).get('HTTP_FUNCTION_EXECUTION_ID')

    def to_json(self):
        all = dict(vars(self), id=self.id)
        public = {k: v for (k, v) in all.items() if not k.startswith('_')}
        return public


go = Gobits()
print(go.to_json())
