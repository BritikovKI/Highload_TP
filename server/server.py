import asyncio
import os
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#TODO: Сделать нормальный логгер если будет время

class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler

    async def subserver_start(self,loop):
        await asyncio.start_server(self.handler,self.host,self.port,loop = loop,reuse_port = True)


    def start(self, cpu, threads):
        subservers = []
        # ADD config faster
        for i in range(0,cpu):
            pid = os.fork()
            subservers.append(pid)
            if pid == 0:
                loop = asyncio.get_event_loop()
                for j in range(0, threads):
                    loop.create_task(self.subserver_start(loop))
                    loop.run_forever()

        for pid in subservers:
            os.waitpid(pid,0)



