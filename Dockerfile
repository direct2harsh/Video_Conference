FROM python:3.13-slim

WORKDIR /app

EXPOSE 8000

COPY . ./

RUN pip install -r requirements.txt

CMD [ "python" ,"main.py" ]