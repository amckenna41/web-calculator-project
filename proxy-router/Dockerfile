#Dockerfile for proxy router microservice 

FROM python:3-alpine

RUN apt-get update -y 
#RUN apt-get update -y && \
 #  apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install Flask
RUN pip install -U flask-cors
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "proxy-router.py" ]
