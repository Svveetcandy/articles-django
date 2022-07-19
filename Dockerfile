
FROM python:3

COPY . /src/articles

WORKDIR /src/articles

RUN pip install -r requirements.txt

RUN chmod +x docker-entrypoint.sh

