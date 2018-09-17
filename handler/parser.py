from models.request import Request

def get_values( data):
    arr = data.split(b'\n')
    values = arr[0].split()
    method = values[0]
    query = values[1].split(b'?')[0]
    protocol =values[2]
    return Request(method,protocol,query,get_connection())


def get_connection():
    return ''