FROM nginx

ARG project_env
# nginx conf
ADD ./docker/nginx/$project_env/default.conf /etc/nginx/sites-enabled/default
ADD ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./app /app

EXPOSE 80 443
