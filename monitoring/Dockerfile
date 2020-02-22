#Docker File for monitoring microservice container

FROM python:3-alpine

RUN apt-get update -y
#RUN apt-get update -y && \
 #  apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -U flask-cors
RUN pip install requests

COPY . /app

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "response_time.py" ]
