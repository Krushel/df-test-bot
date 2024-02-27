from src.sqs import lambda_handler

def test_lambda_handler():
    payload = {'Records': [{'body': open("sqs_message_example.json").read()}]}
    assert lambda_handler(payload, None) is None