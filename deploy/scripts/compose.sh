#!/bin/bash

docker compose \
    --project-directory . \
    -p django \
    -f ./deploy/docker/compose.yaml $@