from models.response import Response

class Serializer:
    def __init__(self):
        pass


    def dump(response):
        if response.status == Response.OK :
            return Serializer.good_resp(response).encode()
        else:
            return Serializer.bad_resp(response).encode()

    def good_resp(response):
        if(response.content_type.split('/')[0] == 'text'):
            body = response.body.decode()
        else:
            body = response.body
        # body = response.body
        return "{} {}\r\n"\
    "Server: {}\r\n"\
    "Date: {}\r\n" \
    "Connection: {}\r\n" \
    "Content-Length: {}\r\n" \
    "Content-Type: {}\r\n\r\n{}".format(response.protocol, response.status,response.server,  response.date, response.connection, response.content_length, response.content_type,body)



    def bad_resp(response):
        return "{} {}\r\n" \
               "Server: {}\r\n" \
               "Date: {}\r\n" \
    "Connection: {}\r\n\r\n".format(response.protocol, response.status, response.server,response.date, response.connection)