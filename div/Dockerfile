#Docker file for divide function in Golang 

FROM golang:latest

RUN mkdir /app

ADD . /app/

WORKDIR /app

COPY go.mod go.sum ./

RUN go build -o main

EXPOSE 8080

CMD ["./main"]