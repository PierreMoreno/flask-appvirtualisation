#Image officielle de Python 3.8 
FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]
