FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip --no-cache-dir install -r requirements.txt

CMD [ "python", "app/app.py" ]