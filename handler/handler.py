
from handler.executor import Executor
from handler.parser import get_values
from handler.serializer import Serializer
import uvloop


def fib( num):
    if num == 1 or num == 0:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

class Handler:

    def __init__(self, root):
        self.root = root
        self.executor = Executor(self.root)


    async def handle(self, reader, writer):
        address = writer.get_extra_info('peername')

        block_size = 1024
        data = b""
        while True:
            block = await reader.read(block_size)
            data += block
            if not block or reader.at_eof():
                break
            if data[-4:] == b'\r\n\r\n':
                break
        if len(data)>0:
            request = get_values(data)
            response = await self.executor.execute(request)
            response_data = Serializer.dump(response)
            writer.write(response_data)
            await writer.drain()
        writer.close()