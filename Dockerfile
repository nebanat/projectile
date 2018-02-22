FROM python:3
MAINTAINER Aaron Biliyok <abiliyok@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

#RUN apk update && apk add build-base postgresql-dev

ENV INSTALL_PATH /projectify
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "projectify.app:create_app()"
