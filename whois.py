import sys
import json

person = sys.argv[1]
print(f'locating secret santa for {person}')

with open('.secret_santas.json') as f:
    people = json.load(f)
    
reciever = next((p['receiver'] for p in people if p['santa'] == person), None)
print(reciever)