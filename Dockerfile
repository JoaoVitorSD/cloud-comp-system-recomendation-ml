FROM python:3.9-slim-bullseye

COPY . /opt/app

WORKDIR /opt/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]