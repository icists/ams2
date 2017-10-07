FROM python:3.6.3-alpine3.6

ADD deployment/pip_requirements.txt /pip_requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            make \
            libc-dev \
            musl-dev \
            linux-headers \
            pcre-dev \
            mariadb-dev \
            jpeg-dev \
            zlib-dev \
    && python -m venv /venv \
    && /venv/bin/pip install -U pip setuptools \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /pip_requirements.txt" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps

RUN mkdir /code/
WORKDIR /code/

ADD ams2/ /code/

# uWSGI will listen on this port
EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
# ENV DJANGO_SETTINGS_MODULE=ams2.settings.deploy

# uWSGI configuration (customize as needed):
ENV UWSGI_VIRTUALENV=/venv \
    UWSGI_WSGI_FILE=ams2/wsgi.py \
    UWSGI_HTTP=:8000 \
    UWSGI_MASTER=1 \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=8 \
    UWSGI_UID=1000 \
    UWSGI_GID=2000 \
    UWSGI_LAZY_APPS=1 \
    UWSGI_WSGI_ENV_BEHAVIOR=holy

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]

