from dotenv import load_dotenv

load_dotenv()
import os
import boto3
import pytest


@pytest.fixture(scope="session")
def dynamodb():
    return boto3.client("dynamodb")


@pytest.fixture(scope="session")
def location_table_name():
    if os.getenv("LOCATION_TABLE_NAME") is None:
        raise ValueError("env LOCATION_TABLE_NAME is not set")
    return os.getenv("LOCATION_TABLE_NAME")
