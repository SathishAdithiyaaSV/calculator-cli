# Use official Python slim image
FROM python:3.11-slim

WORKDIR /app

# copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py .
COPY test_calculator.py .

# default entrypoint runs the CLI (overridden by CI for testing)
ENTRYPOINT ["python", "calculator.py"]
