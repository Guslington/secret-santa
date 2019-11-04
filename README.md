# Secret Santa

Takes a list of names and mobile numbers to sms everybody their secret Santa.

## Requirements

- python 3
- AWS Account

## Setup

install boto3
```bash
pip install --user boto3
```

create the list of people
```bash
cp people.json.example people.json
```

open people.json in your favourite text editor and add the people with their mobile phone numbers
```json
[
  {
    "name": "John",
    "number": "+61400000000"
  },
  {
    "name": "Sally",
    "number": "+61411111111"
  }
]
```

## Generate the list

run
```bash
python generator.py
```

Generates `.secret_santa.json` file with the matches
```json
[
  {
    "santa": "John",
    "reciever": "Sally",
    "number": "+61400000000"
  },
  {
    "santa": "Sally",
    "reciever": "John",
    "number": "+61411111111"
  }
]
```

## Notify

To SMS people their secret Santa

run
```bash
python sms.py
```

to resend a individual person
```bash
python sms.py Sally
```

## Retrieve

To retrieve a specific secret Santa

run
```bash
python whois.py Sally
-> John
```