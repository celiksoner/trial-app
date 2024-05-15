FROM --platform=linux/amd64 python:3.10.10-bullseye
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 3333

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3333"]

