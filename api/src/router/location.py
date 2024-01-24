from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.utilities.parser import parse, envelopes
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventModel
from lib.apigw.envelope import (
    ApiGatewayPathParameterEnvelope,
    ApiGatewayQueryParameterEnvelope,
)
from lib.models import LocationMinimalModel
from pydantic import ValidationError
from lib.dynamodb import dynamodb
import os

router = Router()


@router.get("")
def get_location_minimal():
    """
    拠点のIDと名称の一覧を取得する
    """
    event: dict = router.current_event
    table_name = os.getenv("LOCATION_TABLE_NAME")
    return [
        item.dict()
        for item in LocationMinimalModel.list_from_dynamodb(
            dynamodb, table_name=table_name
        )
    ]
