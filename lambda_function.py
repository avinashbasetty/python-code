import json
import boto3

def lambda_handler(event, context):
    for i in event["Records"]:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name=i["s3"]["bucket"]["name"]
        object_name = i["s3"]["object"]["key"]
        
    client = boto3.client("ses")
    subject = str(action) + 'Event From '+bucket_name
    body="""
    <br>
    This email is to notify you regarding {} event.    
    <br>
    SourceIP : {} <br/>
    Bucket Name : {} <br/>
    Object : {}
    """.format(action,ip,bucket_name,object_name)
    
    message = {"Subject" :{"Data":subject},"Body":{"Html":{"Data":body}}}
    response=client.send_email(Source="avinashbasetty@gmail.com", Destination = {"ToAddresses":["avinashbasetty@gmail.com"]},Message=message)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Notification is successful!')
    }
