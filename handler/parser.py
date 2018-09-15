from models.request import Request

class Parser:
    def get_values(self, data):
        arr = data.split("\n")
        method, query, protocol = self.method_query_protocol(arr[0])

    def method_query_protocol(str_m_q_r):
        list_m_q_r = str_m_q_r.split()
        method = list_m_q_r[0]
        query = list_m_q_r[1]
        protocol = list_m_q_r[2]
        return method, query, protocol

    def url(query):
        list_q_p = query.split("?")
        return list_q_p[0]

    def get_connection(self):
        return ''