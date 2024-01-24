from aws_lambda_powertools.event_handler import ALBResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from router import order_router, location_router
import os

app = ALBResolver()

api_prefix = os.getenv("API_PREFIX", "")
app.include_router(order_router, prefix=f"{api_prefix}/order")
app.include_router(location_router, prefix=f"{api_prefix}/location")


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
