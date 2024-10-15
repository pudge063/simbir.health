FROM python:3.9-slim

RUN pip install uvicorn fastapi

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

