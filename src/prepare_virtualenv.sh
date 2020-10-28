#!/usr/bin/env sh

! [ -d venv ] && python3 -m venv venv || echo "venv already exists"

printf "%s\n\n%s\n\n%s\n\n%s\n\n" '1. run' 'source venv/bin/activate' '2. verify python3 with' 'python --version'
printf "%s\n\n%s\n\n" '3. then run' 'python -m pip install -r requirements.txt'
