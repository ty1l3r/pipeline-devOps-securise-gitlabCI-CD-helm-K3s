FROM python:3.7.7

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV USERS_SERVICE_URL http://users:8000
ENV ORDERS_SERVICE_URL http://orders:8000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD sh -c "uvicorn main:app --reload --host 0.0.0.0"