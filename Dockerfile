FROM python:3.8.5

WORKDIR /streaming-ms-api
COPY . .
RUN pip install -r requirements.txt

CMD python ./service.py