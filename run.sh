#!/usr/bin/env bash
python3 -m pip install --user virtualenv
mkdir -p .venvs
python3 -m venv .venvs/phonehome
source .venvs/phonehome/bin/activate
python3 phonehome.py
