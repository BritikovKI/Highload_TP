from models.response import Response,OK

class Serializer:
    def __init__(self):
        pass

    @staticmethod
    def dump(response):
        if response.status == OK :
            return Serializer.good_resp(response).encode() +response.body
        else:
            return Serializer.bad_resp(response).encode()

    def good_resp(response):
        return "{} {}\r\n"\
    "Server: {}\r\n" \
    "Date: {}\r\n" \
    "Connection: {}\r\n" \
    "Content-Length: {}\r\n" \
    "Content-Type: {}\r\n\r\n".format(response.protocol, response.status_code, response.server, response.date, response.connection, response.content_length, response.content_type)



    def bad_resp(response):
        return "{} {}\r\n" \
    "Server: {}\r\n" \
    "Date: {}\r\n" \
    "Connection: {}\r\n\r\n".format(response.protocol, response.status_code, response.server, response.date, response.connection)