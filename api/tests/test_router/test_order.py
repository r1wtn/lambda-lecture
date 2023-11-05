from main import lambda_handler


def test_order(lambda_context, base_event: dict):
    base_event["path"] = "/order"
    base_event["pathParameters"] = {"order_id": "1"}
    base_event["queryStringParameters"] = {"product_id": 1, "number": 1}
    res = lambda_handler(base_event, lambda_context)
    assert res["statusCode"] == 200
    assert res["body"] == '{"product_id":1,"number":1,"user_id":null}'
