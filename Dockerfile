FROM ubuntu:16.04

RUN apt-get -y update &&\
        apt-get -y upgrade &&\
        apt-get -y install python3-pip

RUN pip3 install asyncio &&\
        pip3 install uvloop &&\
        pip3 install aiofiles &&\
        pip3 install urllib3

RUN apt-get -y install apache2-utils

ADD . .

RUN mkdir -p /home/chapay/TechPark/Highload/tests
COPY ./tests/ /home/chapay/TechPark/Highload/tests

COPY ./test_config /


EXPOSE 80

CMD python3 source/main.py
