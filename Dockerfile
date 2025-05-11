FROM python:3.11-slim

# 기본 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 필요 시 .env 파일도 추가
# COPY .env .env

CMD ["python", "app.py"]
