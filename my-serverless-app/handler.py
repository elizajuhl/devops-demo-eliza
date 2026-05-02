import json

def hello(event, context):
    name = event.get("name", "stranger")
    temperature = event.get("temperature", 20)

    if temperature > 30:
       status = "Too hot!"
    else:
       status = "Normal"

    body = {
        "message": f"Hello {name}, your serverless function worked!",
        "temperature": temperature, 
        "status": status,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
