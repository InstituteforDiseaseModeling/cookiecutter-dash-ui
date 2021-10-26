#!/bin/bash

if [ "$DEBUG" = "1" ]; then
    echo "Running Debug Server"
    export PYTHONPATH=/app
    cd /app/service
    python main.py
else
    echo "Launching Gunicorn"
    cd /app/service
    gunicorn main:server -b 0.0.0.0:8050 --timeout 120
fi