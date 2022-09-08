# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/anime_media
ADD . /usr/src/anime_media

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/anime_media/docker-entrypoint.sh

ENTRYPOINT ["/usr/src/anime_media/docker-entrypoint.sh"]