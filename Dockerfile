FROM 364843010988.dkr.ecr.eu-west-1.amazonaws.com/base_python:master
MAINTAINER Aidan OFlannagain

ADD . .

RUN apt-get update
RUN apt-get install -y libmysqlclient-dev
RUN pip install --upgrade -r requirements.txt

CMD ["/usr/bin/python main.py"]