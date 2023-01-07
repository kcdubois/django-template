#!/bin/bash

echo "Building project using the django project name"
docker compose \
    --project-directory . \
    -p django \
    -f ./deploy/docker/compose.yaml build \


echo "Starting Docker Compose for development"
docker compose \
    --project-directory . \
    -p django \
    -f ./deploy/docker/compose.yaml up \
    --detach
