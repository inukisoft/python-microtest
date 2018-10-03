FROM python:3.6

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN pip install -r requirements.txt

EXPOSE 9090
cmd ["python","/code/app.py"]