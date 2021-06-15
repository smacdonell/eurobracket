from threading import local

"""
Custom middleware that can be used to store and retrieve data in the local thread
"""


class ApplicationHelper:
    _thread_local = local()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(self._thread_local, 'request', request)

        response = self.get_response(request)

        return response

    @classmethod
    def get_request(cls):
        return getattr(cls._thread_local, 'request', None)

    @classmethod
    def set_data(cls, key, value):
        setattr(cls._thread_local, key, value)

    @classmethod
    def get_data(cls, key):
        return getattr(cls._thread_local, key, None)

    @classmethod
    def set_session_data(cls, key, value):
        setattr(cls.get_request().session, key, value)

    @classmethod
    def get_session_data(cls, key):
        return getattr(cls.get_request().session, key, None)

    @classmethod
    def set_spotify_auth(cls, auth):
        setattr(cls.get_request().session, 'spotify_auth', auth)

    @classmethod
    def get_spotify_auth(cls):
        return getattr(cls.get_request().session, 'spotify_auth', None)
