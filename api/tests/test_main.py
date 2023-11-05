from main import lambda_handler


def test_lambda_handler(
    lambda_context,
):
    test_event = {"test": "event"}
    lambda_handler(test_event, lambda_context)
