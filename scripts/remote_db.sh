#!/usr/bin/env bash

docker run --rm -it postgis/postgis:13-3.1-alpine psql -h census-db -U postgres -d census_canada
