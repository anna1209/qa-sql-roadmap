# conftest.py
import os
import pymysql
import pytest
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

@pytest.fixture(scope="function")
def db_connection():
    conn = pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        autocommit=False,
    )
    yield conn