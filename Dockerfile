FROM python:3.9

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . .
RUN python manage.py migrate
RUN python manage.py loaddata seed.json
RUN chmod +x *.sh

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]