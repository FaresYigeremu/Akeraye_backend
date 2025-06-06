FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/akeraye_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get install -y --no-install-recommends build-essential libyaml-dev

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/akeraye_backend/entrypoint.sh" ]
