FROM python:3.11.7

WORKDIR /FlaskApp

COPY . .

RUN pip install flask

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]