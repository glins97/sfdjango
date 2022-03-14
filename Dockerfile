FROM python:3.9

RUN apt-get -y update && apt-get -y install openjdk-11-jre-headless
ENV JAVA_HOME = /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . .
#RUN python manage.py shell < ./databases/loadSemanticDatabase.py
RUN python manage.py migrate
RUN python manage.py loaddata seed.json
RUN chmod +x *.sh

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]