class HTTPError(Exception):
    def __init__(self, response, msg=None):
        if msg is None:
            message = "Http exception has occurred: [{}]".format(response)
        else:
            message = msg
        super(HTTPError, self).__init__(message)
        self.message = str(message)
        self.response = response


class AccessError(Exception):
    def __init__(self, message):
        super(AccessError, self).__init__(message)
        self.message = str(message)


class SteamIdError(Exception):
    def __init__(self, message):
        super(SteamIdError, self).__init__(message)
        self.message = str(message)

