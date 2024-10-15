FROM python:3.9-slim

RUN pip install uvicorn fastapi pydantic-settings sqlalchemy psycopg2-binary passlib python-jose

WORKDIR /app

COPY ./account-microservice/app .

COPY .env .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

