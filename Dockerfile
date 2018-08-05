FROM ubuntu:latest
MAINTAINER Lee Thompson "biofects@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-crypto python3-flask  python-pip python-dev build-essential
WORKDIR /app
RUN pip install flask requests request
COPY . /app
ENTRYPOINT ["python3"]
CMD ["api.py"]
