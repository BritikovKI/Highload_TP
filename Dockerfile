#FROM ubuntu:16.04
#MAINTAINER Britikov Konstantin
#RUN apt-get update -y
#
#RUN apt-get install -y python3
#
#ADD ./Highload  /coro_server
#ADD ./httptest /var/www/html/httptest/
#
#EXPOSE 80
#
#CMD python3 /coro_server/main.py