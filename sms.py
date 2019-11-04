import boto3
import json
import sys

person = None

if len(sys.argv) > 1:
    person = sys.argv[1]
    print(f'sending secret santa for {person}')

with open('.secret_santas.json') as f:
    secret_santas = json.load(f)

if person:
    secret_santas = [p for p in secret_santas if p['santa'] == person]

client = boto3.client('sns')
for secret_santa in secret_santas:
    print(f"sending secret santa to {secret_santa['santa']}")
    sms_message = f"Your secret santa for Christmas this year is {secret_santa['reciever']}"
    client.publish(
        PhoneNumber=secret_santa['number'], 
        Message=sms_message, 
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String', 
                'StringValue': 'SecretSanta'
            }, 
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String', 
                'StringValue': 'Promotional'
            }
        }
    )