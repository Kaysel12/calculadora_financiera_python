FROM python:3.12.5-alpine3.20

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev libffi-dev mysql-client\
    && apk add --no-cache mariadb-dev \
    && pip install --upgrade pip setuptools 

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
