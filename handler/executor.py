from models.response import Response

from handler.errors import ForbidenError,NotFoundError
from models.file import File
import os
import aiofiles
import urllib.parse
from pymemcache.client import base


class Executor:
    def __init__(self,files):
        self.files_root = files
        self.client = base.Client(('localhost' ,11211))
    content_types = {
        'html': 'text/html',
        'txt': 'text/txt',
        'css': 'text/css',
        'js': 'text/javascript',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'swf': 'application/x-shockwave-flash'
    }

    async def execute(self, request):
        if request.method not in [b'GET',b'HEAD']:
            return Response(Response.METHOD_NOT_ALLOWED, request.protocol,connection = request.connection)
        elif request.method == b'HEAD':
            return await self.execute_head(request)
        else:
            return await self.execute_get(request)


    async def execute_head(self, request):
        try:
            file = self.get_file_info(request)
        except ForbidenError:
            return Response(status = Response.FORBIDDEN, protocol = request.protocol, connection='')
        except NotFoundError:
            return Response(status = Response.NOT_FOUND, protocol = request.protocol, connection='')
        return Response(status=Response.OK, protocol=request.protocol, connection='closed', content_length=file.content_length, content_type=file.content_type)

    async def execute_get(self,request):


        try:
            file = self.get_file_info(request)
            body = await self.read_file(file.filename)
            return Response(status = Response.OK, protocol = request.protocol, connection='closed',content_type=file.content_type,content_length=file.content_length,
                            body=body)
        except ForbidenError:
            return Response(status = Response.FORBIDDEN, protocol = request.protocol, connection='')
        except NotFoundError:
            return Response(status = Response.NOT_FOUND, protocol = request.protocol, connection='')







    def get_file_info(self,request):
        file_path = request.get_url().decode()
        file_path = urllib.parse.unquote(file_path, encoding='utf-8',errors='replace')
        if len(file_path.split( '../')) > 1:
            raise ForbidenError
        if file_path[-1:] ==  '/':
            file = self.files_root + file_path + "index.html"
        else:
            file = self.files_root + file_path


        if file.split('.')[-1:][0] in self.content_types:
            content = self.content_types[file.split('.')[-1]]
        else:
            content = ''
        if not os.path.isfile(file):
            if file_path[-1:] == '/' and file_path.count(".") < 1:
                raise ForbidenError
            else:
                raise NotFoundError
        return File(filename=file,file_path=file_path,content_type=content,content_length = os.path.getsize(file))


    async def read_file(self,filename):
        async with aiofiles.open(filename, mode='rb') as file:
            return await file.read()
