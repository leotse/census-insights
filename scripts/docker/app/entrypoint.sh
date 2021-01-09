#!/usr/bin/env bash

pip install -r /src/requirements.txt

uvicorn api.main:app --host 0.0.0.0 --reload
