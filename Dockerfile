FROM python:3.9-slim-bullseye

RUN pip3 install

ENTRYPOINT ["python3", "main.py"]