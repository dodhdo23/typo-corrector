FROM python:3.10-slim

WORKDIR /app

# 의존성 먼저 설치
COPY requirements.txt ./
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 필요한 파일만 복사
COPY app.py ./
COPY checkpoint/ ./checkpoint/
COPY et5_model/ ./et5_model/

EXPOSE 5000

CMD ["python", "app.py"]
