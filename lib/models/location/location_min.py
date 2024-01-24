from pydantic import BaseModel
from boto3.session import Session
from typing import Optional, List


class LocationMinimalModel(BaseModel):
    location_id: str
    location_name: str

    @classmethod
    def list_from_dynamodb(
        cls, dynamodb: Session, table_name: Optional[str] = "locations"
    ):
        query_option = {
            "TableName": table_name,
            "IndexName": "GSI-1-index",
            "KeyConditionExpression": "DataType = :data_type",
            "ExpressionAttributeValues": {":data_type": {"S": "Location"}},
            "ProjectionExpression": "LocationId, LocationName",
        }
        response = dynamodb.query(**query_option)
        items = response["Items"]
        location_min_list = []
        for item in items:
            if item.get("LocationId") is None:
                continue
            if item.get("LocationName") is None:
                continue
            location_min_list.append(
                {
                    "location_id": item["LocationId"]["S"],
                    "location_name": item["LocationName"]["S"],
                }
            )
        return location_min_list
