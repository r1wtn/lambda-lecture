from aws_lambda_powertools.event_handler.api_gateway import Router

router = Router()



@router.get("/todos")
def get_todos():
    return {"todos": None}
