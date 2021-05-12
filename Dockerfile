FROM ubuntu:20.04

LABEL \
    maintainer="Tuhin Paul" \
    phone="+1 778 201 8345" \
    email="tuhin[DOT]paul[AT]usask[DOT]ca"

RUN apt-get update -y

# ubuntu 20.04 ships with pre-installed python3
# install pip3 for python3
RUN apt-get install -y python3-pip

WORKDIR /flask-sample-project
COPY . ./
# psycopg2 requires pg_config, which is in is in postgresql-devel (libpq-dev in Debian/Ubuntu)
RUN apt-get install -y libpq-dev
RUN pip3 install -r dockerPipRequirements

ENV FLASK_APP=flaskr
ENV FLASK_ENV=production
ENV FLASK_RUN_PORT=80

# temporary configurations for showing sample
ENV FLASK_SAMPLE_INITIALIZE_DATABASE=true
ENV FLASK_SAMPLE_CREATE_DUMMY_DATA=true

EXPOSE 80

ENTRYPOINT ["python3"]

CMD [ "-m", "flask", "run" ]
