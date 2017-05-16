FROM 364843010988.dkr.ecr.eu-west-1.amazonaws.com/base_python:master
MAINTAINER Aidan OFlannagain

RUN apt-get update
RUN pip install --upgrade -r requirements.txt

ADD .

CMD ["/bin/bash"]