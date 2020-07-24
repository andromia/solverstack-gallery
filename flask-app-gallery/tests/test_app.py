#!/usr/bin/env python
import logging

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from config import Config

import pytest


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

@pytest.fixture
def client():
    yield create_app(TestConfig).test_client()

@pytest.mark.filterwarnings
def test_main_procedure(client):
    pass
