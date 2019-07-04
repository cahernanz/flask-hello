FROM python:3-slim

WORKDIR /app
COPY . /app

#RUN apt update && apt install -y curl

RUN pip install -r requirements.txt
RUN pip install -e .

EXPOSE 80
ENV NAME techonwheels

CMD ["flask_hello"]
