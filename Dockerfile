FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip isntall --no-cache-dir requirements.txt
COPY . .
EXPOSE 8082
CMD [ "python","main.py" ]
