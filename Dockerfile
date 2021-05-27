# Use an official Python runtime as a parent image
FROM python:3.8

RUN apt-get update \
    && apt-get install dos2unix \
    && apt-get install -y cron && apt-get install -y vim \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Add crontab file in the cron directory
COPY predict_job /etc/cron.d/predict_job

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/predict_job

RUN crontab /etc/cron.d/predict_job

RUN touch /var/log/cron.log

ADD ./run_predict.sh /app/run_predict.sh

RUN chmod +x /app/run_predict.sh

RUN dos2unix /app/run_predict.sh

EXPOSE 5000

CMD ["python", "app.py"]
