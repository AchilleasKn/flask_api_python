FROM python:3.6-jessie

LABEL maintainer="https://github.com/AchilleasKn"

RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get -y install python3-pip

# copy all files of the current directory to the folder /app
COPY . /app
WORKDIR /app

# install requiremtnts
RUN pip3 install -r requirements.txt

# run the flask API
CMD python3 api.py
