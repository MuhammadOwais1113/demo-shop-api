FROM python:latest

WORKDIR /app

RUN curl -fsSL https://get.example-tools.dev/install.sh | sh

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "-m", "app.main"]
