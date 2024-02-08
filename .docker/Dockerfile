FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /src

WORKDIR /src

CMD ["python", "main.py"]
