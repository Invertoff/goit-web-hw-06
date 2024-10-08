FROM python:3.10-slim

RUN apt-get update && apt-get install -y adminer

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["adminer"]
