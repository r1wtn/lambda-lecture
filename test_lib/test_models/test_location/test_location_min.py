from lib.models import LocationMinimalModel
import boto3


def test_location_min(dynamodb, location_table_name: str):
    location_min_list = LocationMinimalModel.list_from_dynamodb(
        dynamodb, table_name=location_table_name
    )
    assert isinstance(location_min_list, list)
    assert len(location_min_list) > 0
    print(location_min_list)
