
FROM python:3.12

ENV PYTHONBUFFERED=1

# Allows docker to cache installed dependencies between builds
COPY requirements.txt .
RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "schooldata/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]