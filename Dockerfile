FROM tiangolo/uwsgi-nginx:python3.8

# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENV STATIC_URL /static
ENV STATIC_PATH /app/static
