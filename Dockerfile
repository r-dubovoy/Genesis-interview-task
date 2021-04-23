FROM python:3.7

RUN apt-get update -y

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get -y install cmake protobuf-compiler
RUN pip3 install -r requirements.txt

RUN pip3 install torch==1.7.0 torchvision==0.8.1 torchaudio===0.7.0

EXPOSE 5000

CMD python main.py