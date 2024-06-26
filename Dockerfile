FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
