FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

ENV PORT=8000

CMD ["uvicorn", "challenge_2:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
