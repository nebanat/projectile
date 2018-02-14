FROM python:3
MAINTAINER Aaron Biliyok <abiliyok@gmail.com>

ENV INSTALL_PATH /projectify
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "projectify.app:create_app()"
