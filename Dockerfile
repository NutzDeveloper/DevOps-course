FROM python:alpine
RUN pip install pytest
COPY . .
CMD ["pytest", "app.py"]