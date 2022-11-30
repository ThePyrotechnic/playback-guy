FROM python:3.10-alpine as build

ARG VERSION
ARG WHEEL

WORKDIR /

RUN apk update; apk add \
    ffmpeg opus-dev cargo rust cmake

ENV PATH=/venv/bin:$PATH
RUN python -m venv venv; \
    pip install --upgrade pip; pip install \
        youtube_dl

COPY dist/$WHEEL $WHEEL

RUN pip install ./$WHEEL

FROM python:3.10-alpine

WORKDIR /

RUN apk update; apk add \
    ffmpeg opus

COPY --from=build /venv venv
COPY secret.key secret.key

ENV PATH=/venv/bin:$PATH

ENTRYPOINT [ "playback-guy" ]
CMD [ "start" ]
