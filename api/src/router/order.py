from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.utilities.parser import parse, envelopes
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventModel
from lib.apigw.envelope import (
    ApiGatewayPathParameterEnvelope,
    ApiGatewayQueryParameterEnvelope,
)
from lib.models import OrderQueryParameter, OrderPathParameter
from pydantic import ValidationError

router = Router()


@router.get("")
def get_order():
    event: dict = router.current_event
    path_parameters: OrderPathParameter = parse(
        model=OrderPathParameter, event=event, envelope=ApiGatewayPathParameterEnvelope
    )
    query_parameters: OrderQueryParameter = parse(
        model=OrderQueryParameter,
        event=event,
        envelope=ApiGatewayQueryParameterEnvelope,
    )

    # DBでふぃるた
    product_id = query_parameters.product_id
    number = query_parameters.number
    return query_parameters.dict()
