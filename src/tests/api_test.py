from src.api import lambda_handler

def test_lambda_handler():
    payload = {'body': open("telegram_request_example.json").read()}
    assert lambda_handler(payload, None) == {'statusCode': 200, 'body': 'Success'}

def test_lambda_handler_failure():
    payload = {'body': 'mocked failure message'}
    assert lambda_handler(payload, None) == {'statusCode': 500, 'body': 'Failure'}