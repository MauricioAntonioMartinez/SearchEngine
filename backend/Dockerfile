FROM python:3.9-alpine


RUN  pip3 install --upgrade pip


WORKDIR /app

COPY /requirements.txt /app

RUN pip3 install -r requirements.txt

COPY /app .

EXPOSE 5000


ENTRYPOINT [ "python3" ]

CMD ["main.py"]
