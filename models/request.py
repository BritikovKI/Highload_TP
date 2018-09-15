class Request:

    def __init__(self, method, protocol, url, connection):
        self.method = method
        self.protocol = protocol
        self.url = url
        self.connection = connection

    def get_method(self):
        return self.method

    def get_protocol(self):
        return self.protocol

    def get_url(self):
        return self.url

    def get_connection(self):
        return self.connection

