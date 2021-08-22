FROM python:3-alpine

FROM wize-David-Vanegas:latest
COPY main.py /
CMD [ "wize-David-Vanegas", "./main.py" ]

