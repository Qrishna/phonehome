import json
import logging
import os
import platform
import time
from unittest.mock import patch, Mock
import pytest
import psutil
import requests_mock
import re
from datetime import datetime, timezone, timedelta
from phonehome import *


def test_get_utc_timestamp():
    # Test that the timestamp is in the correct format
    timestamp = get_utc_timestamp()
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+00:00", timestamp)


def test_get_utc_timestamp_format():
    # Test that the timestamp is in the correct format
    timestamp = get_utc_timestamp()
    assert datetime.fromisoformat(timestamp) - datetime.now(timezone.utc) < timedelta(seconds=1)


def test_get_utc_timestamp_accuracy():
    # Test that the timestamp is accurate to within 1 second
    timestamp1 = get_utc_timestamp()
    timestamp2 = get_utc_timestamp()
    diff = abs((datetime.fromisoformat(timestamp1) - datetime.fromisoformat(timestamp2)).total_seconds())
    assert diff < 1.0
