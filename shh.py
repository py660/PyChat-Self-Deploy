# type: ignore
import json

fin = open("secrets.json")
raw_data = fin.read()
#print(raw_data)
environ_data = json.loads(raw_data)

def load(os, db):
    for i in environ_data:
        os.environ[i] = environ_data[i]
