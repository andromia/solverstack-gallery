FROM python:3.8-slim

COPY requirements*.txt /app/

WORKDIR /app

RUN python -m pip install -r requirements.txt

RUN python -m pip install -r requirements-dev.txt

COPY . /app

ENV FLASK_APP app
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

ENTRYPOINT [ "python" ]

# Set and expose port
ENV PORT 5000
EXPOSE 5000