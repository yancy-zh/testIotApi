import requests
import json
import resource.statuscode as statuscode
"""
This class provides a connection to the cloud based on directus. 
"""

class Connection:

    def __init__(self, host, port=None, project = None, secure_connection=False, user_email = None, password = None, token = None):
        self.host              = host
        self.port              = port
        self.project = project
        self.user_email = user_email
        self.password = password
        self.secure_connection = secure_connection
        self.token = token
        if secure_connection:
            self.protocol = 'https'
            if self.port is None or self.port == -1:
                self.port = 443
        else:
            self.protocol = 'http'
            if self.port is None or self.port == -1:
                self.port = 80

        self.temp_token = self.retrieve_init_token()
# need to modify
    def url(self, api_url):
        if api_url[0] == '/':
            return "{0}://{1}:{2}/{3}{4}".format(self.protocol, self.host, self.port, self.project, api_url)
        else:
            return "{0}://{1}:{2}/{3}/{4}".format(self.protocol, self.host, self.port, self.project, api_url)

    def retrieve_init_token(self):
        temp_authen_info = {
            "email": self.user_email,
            "password": self.password
        }
        # get the token from the retrieved data for the authorized user
        token = requests.post(self.url("/auth/authenticate"),
                               json = temp_authen_info).json()["data"]["token"]
        return token

    def refresh_token(self, httpargs):
        new_token = requests.post(self.url("/auth/refresh"),
                               json = {"token": self.temp_token}).json()["data"]["token"]
        tmp = {'Authorization' : "Bearer "+ new_token}
        try:
            h = httpargs.pop('headers')
            tmp.update(h)
        except KeyError:
            pass

        httpargs.update({ 'headers' : tmp })

        return httpargs

    def authorize(self, httpargs):
        temp_authen_info = {
            "email": self.user_email,
            "password": self.password
        }
        # get the token from the retrieved data for the authorized user
        token = requests.post(self.url("/auth/authenticate"),
                               json = temp_authen_info).json()["data"]["token"]

        tmp = {'Authorization' : "Bearer "+ token}
        try:
            h = httpargs.pop('headers')
            tmp.update(h)
        except KeyError:
            pass

        httpargs.update({ 'headers' : tmp })

        return httpargs

    """
        Executes a GET request.
        :param api_url: a url defined in the api reference
        :param **kwargs: Optional arguments that will pass to original request object
        :return: a Response object containing original request response
    """
    def send_get_request(self, api_url, **kwargs):
        return Response(requests.get(self.url(api_url), **self.refresh_token(kwargs)))

    """
        Executes a POST request.
        :param api_url: a url defined in the api reference
        :param **kwargs: Optional arguments that will pass to original request object
        :return: a Response object containing original request response
    """
    def send_post_request(self, api_url, **kwargs):
        return Response(requests.post(self.url(api_url), **self.refresh_token(kwargs)))

    """
        Executes a PATCH request.
        :param api_url: a url defined in the api reference
        :param **kwargs: Optional arguments that will pass to original request object
        :return: a Response object containing original request response
    """
    def send_patch_request(self, api_url, **kwargs):
        return Response(requests.patch(self.url(api_url), **self.refresh_token(kwargs)))

    """
        Executes a DELETE request.
        :param api_url: a url defined in the api reference
        :param **kwargs: Optional arguments that will pass to original request object
        :return: a Response object containing original request response
    """
    def send_delete_request(self, api_url, **kwargs):
        return Response(requests.delete(self.url(api_url), **self.refresh_token(kwargs)))

"""
    The Response class wraps requests.Response.
"""
class Response:
    def __init__(self, response):
        self.response = response
        try:
            self.data     = response.json()
            self.status   = response.status_code

        except json.JSONDecodeError:
            self.data    = None
            self.status  = None

    @property
    def request(self):
        return self.response.request

    @property
    def request_path_url(self):
        return self.response.request.path_url

    @property
    def request_body(self):
        return self.response.request.body

    @property
    def status_code(self):
        if self.response is not None:
            return self.response.status_code
        else:
            return -1

    @property
    def status_message(self):
        if self.response is not None:
            return self.response.reason
        else:
            return "Invalid response."

    @property
    def response_content(self):
        return self.response.content
