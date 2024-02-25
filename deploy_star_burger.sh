#!/bin/bash

set -e

PROJECT_DIR=$(pwd)
ENV_FILE="$PROJECT_DIR/.env"

source "$ENV_FILE"

echo "Обновление кода из репозитория..."
git pull

echo "Пересборка Docker образов"
docker-compose -f $PROJECT_DIR/docker-compose.yml build

echo "Перезапуск контейнеров"
docker-compose -f $PROJECT_DIR/docker-compose.yml down
docker-compose -f $PROJECT_DIR/docker-compose.yml up -d

docker cp production_env_django_1:/app/staticfiles /var/www/starburger/
docker cp production_env_frontend_1:/app/bundles/. /var/www/starburger/staticfiles

systemctl reload nginx

commit=`git rev-parse HEAD`

echo "Отправка уведомления в Rollbar..."
curl -H "X-Rollbar-Access-Token: $ROLLBAR_ACCESS_TOKEN" \
     -H "accept: application/json" \
     -H "content-type: application/json" \
     -X POST "https://api.rollbar.com/api/1/deploy" \
     -d '{
  "environment": "production",
  "revision": "'$commit'",
  "rollbar_username": "admin",
  "local_username": "admin",
  "comment": "deploy",
  "status": "succeeded"
}'

echo "Деплой завершен успешно."
