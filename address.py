# create address book and write records
# read the address book

book = {}
book["tom"] = {
    "name": "tom",
    "address": "1 Red Street, NY",
    "phone": 256852856954
}

book["bob"] = {
    "name": "bob",
    "address": "1 Green Street, NY",
    "phone": 256021745632
}

import json
s = json.dumps(book)
with open("C://Users//Waburi Brian//PycharmProjects//Data//book.txt","w") as f:
    f.write(s)

