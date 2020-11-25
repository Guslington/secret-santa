import json
from random import choice

with open('people.json') as f:
    people = json.load(f)

while True:
    santas = [person for person in people]
    received = []
    results = []

    for i in range(len(santas)):
        santa = choice(santas)
        receivers = [person for person in people 
                                if person['name'] != santa['name']
                                and person['name'] not in received 
                                and santa['name'] not in person['previous']]
        if not receivers:
            break

        receiver = choice(receivers)

        results.append({
            'santa': santa['name'],
            'receiver': receiver['name'],
            'number': santa['number']
        })

        santas.remove(santa)
        received.append(receiver['name'])

    if len(results) == len(people):
        break

    
with open('.secret_santas.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
