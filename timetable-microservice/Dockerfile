FROM python:3.9-slim

RUN pip install uvicorn fastapi pydantic-settings

WORKDIR /app

COPY ./timetable-microservice .

COPY .env .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

