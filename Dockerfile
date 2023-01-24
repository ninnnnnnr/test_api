FROM python:3.10.0

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "start_app:app", "--host", "0.0.0.0", "--port", "8000"]

