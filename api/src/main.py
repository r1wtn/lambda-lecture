from aws_lambda_powertools.event_handler import ALBResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from router import order_router

app = ALBResolver()

app.include_router(order_router, prefix="/order")


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
