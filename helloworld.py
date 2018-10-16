def lambda_handler(event, context):
    c = event['a'] + event['b']
    return c
