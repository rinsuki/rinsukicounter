FROM python:3.6

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

ENV TZ=Asia/Tokyo

COPY . /app/

CMD ["python3", "main.py"]