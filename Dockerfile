FROM python:3.10-alpine

ARG VERSION
ARG WHEEL

WORKDIR /

RUN apk update; apk add \
    ffmpeg opus-dev cargo rust cmake

RUN pip install --upgrade pip; pip install \
    youtube_dl

COPY dist/$WHEEL $WHEEL

RUN pip install ./$WHEEL

COPY secret.key secret.key

ENTRYPOINT [ "python", "-m", "playback_guy" ]
CMD [ "start" ]
