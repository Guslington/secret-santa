import json
import boto3
from random import shuffle

with open('people.json') as f:
    people = json.load(f)

def match(people):
    receivers = [person['name'] for person in people]
    santas = [person['name'] for person in people]
    shuffle(receivers)
    results = []
    for i, receiver in enumerate(receivers):
        results.append({
            'santa': santas[i],
            'reciever': receiver,
            'number': people[i]['number']
        })
    return results

def duplicate(secret_santas):
    for secret_santa in secret_santas:
        if secret_santa['reciever'] == secret_santa['santa']:
            print(f"found duplicate: {secret_santa['reciever']} {secret_santa['santa']}")
            return True
    return False

while True:
    secret_santas = match(people)
    if not duplicate(secret_santas):
        break
    
with open('.secret_santas.json', 'w', encoding='utf-8') as f:
    json.dump(secret_santas, f, ensure_ascii=False, indent=4)
