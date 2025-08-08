FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
