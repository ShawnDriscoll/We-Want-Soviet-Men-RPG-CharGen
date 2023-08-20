
import json
import pprint

with open('We Want Soviet Men Characters/Sample Char.tps', 'r') as json_file:
    data = json.load(json_file)

    pprint.pprint(data)
