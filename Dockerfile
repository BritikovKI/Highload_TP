FROM ubuntu:16.04

RUN apt-get -y update &&\
        apt-get -y upgrade &&\
        apt-get -y install python3-pip &&\
        apt-get -y install memcached

RUN pip3 install asyncio &&\
        pip3 install uvloop &&\
        pip3 install aiofiles &&\
        pip3 install urllib3 &&\
        pip3 install pymemcache

#RUN apt-get -y install apache2-utils

ADD . .

EXPOSE 80

RUN memcached

CMD python3 main.py

