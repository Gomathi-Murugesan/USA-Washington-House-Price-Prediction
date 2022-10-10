FROM python:3.7

RUN apt-get update

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt

COPY . /api
WORKDIR /

EXPOSE $port

CMD ["gunicorn", "-w", "3", "-b", --port $PORT, "-t", "360", "--reload", "api.wsgi:app"]