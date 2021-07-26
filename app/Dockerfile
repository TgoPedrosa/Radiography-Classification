# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
ENV PORT 8501
#EXPOSE 8501

COPY . .

#ENTRYPOINT ["streamlit", "run"]

CMD streamlit run app.py --server.port $PORT 
