#!/bin/bash
set -e

echo "Waiting for Redis..."
until redis-cli -h redis ping | grep PONG; do
  sleep 1
done

echo "Waiting for PostgreSQL..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -c '\q'; do
  sleep 1
done

echo "All services are up!"

