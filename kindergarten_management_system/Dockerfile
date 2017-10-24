 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /kms
 WORKDIR /kms
 ADD requirements.txt /kms/
 RUN pip install -r requirements.txt
 ADD . /kms/
 COPY ./docker-entrypoint.sh /
 RUN ["chmod", "+x", "/docker-entrypoint.sh"]
 ENTRYPOINT ["/docker-entrypoint.sh"]
