import requests


def request_method(method):
    def decorator(response):
        def wrapper(*arg, **kwargs):
            return requests.request(method, *arg, **kwargs)
        return wrapper
    return decorator


@request_method("POST")
def create_(self, url, headers, auth, json, timeout=7):
    pass


@request_method("GET")
def read_(self, url, headers, auth, json, timeout=7):
    pass


@request_method("PUT")
def update_(self, url, headers, auth, json, timeout=7):
    pass


@request_method("DELETE")
def delete_(self, url, headers, auth, json, timeout=7):
    pass
