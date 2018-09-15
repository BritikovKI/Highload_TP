from datetime import datetime


OK = '200'
NOT_FOUND = '404'
METHOD_NOT_ALLOWED = '405'
FORBIDDEN = '403'


class Response:
    def __init__(self, status, protocol,content_type, content_length, body):
        self.status = status
        self.protocol = protocol
        self.content_type = content_type
        self.content_length = content_length
        self.body = body
        # self.date = Response.timestamp()


    def get_status(self):
        return self.status


    def get_protocol(self):
        return self.protocol


    def get_content_type(self):
        return self.content_type


    def get_content_length(self):
        return self.content_length


    def get_body(self):
        return self.body
