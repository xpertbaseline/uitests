FROM python:alpine3.10
MAINTAINER xpertbaseline@gmail.com
RUN apk update -qq && apk add --update build-base git bash jq
RUN apk add libffi openssl bash curl gcc libffi-dev musl-dev openssl-dev make
RUN pip install --upgrade pip
RUN pip3 install selenium
RUN pip3 install pyyaml
WORKDIR /opt
COPY . /opt/
RUN chmod +x HoeWarmIsHetInDelft.py
