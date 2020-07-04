FROM python:latest

ENV SECRET_KEY test
ENV DEBUG True
ENV ALLOWED_HOSTS *
ENV SLACK_BOT_USER_OAUTH_ACCESS_TOKEN bot_token
ENV SLACK_CLIENT_ID client_id
ENV SLACK_CLIENT_SECRET client_secret
ENV SLACK_VERIFICATION_TOKEN verification_token

RUN mkdir /cryptprice

ADD ./app /cryptprice
ADD requirements.txt /cryptprice/requirements.txt
RUN pip install -r /cryptprice/requirements.txt

RUN apt-get -y update && apt-get -y autoremove
WORKDIR /cryptprice

EXPOSE 8000

CMD gunicorn -b :8000 core.wsgi
