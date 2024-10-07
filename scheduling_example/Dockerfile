FROM python:3.8

COPY crontab /etc/cron.d/my-cron
RUN chmod 644/etc/cron.d/my-cron

RUN apt update
RUN apt install -y cron

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
CMD ["/bin/bash"]
