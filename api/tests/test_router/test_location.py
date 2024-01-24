from main import lambda_handler
import pytest
import json


@pytest.fixture(scope="function")
def location_event(base_event: dict):
    base_event["path"] = "/location"
    base_event["pathParameters"] = {}
    return base_event


def test_location_minimal(lambda_context, location_event: dict):
    res = lambda_handler(location_event, lambda_context)
    assert res["statusCode"] == 200
    body = json.loads(res["body"])
    print(body)
    assert len(body) > 0
