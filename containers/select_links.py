import json
import re

data = json.load(open('links.json'))
table = []

for link in data:
    if re.match("^https://moverdb.com/freight-costs", link['link']) is not None:
        table.append(link['link'])

with open("selected_links.json", "wb") as f:
    json.dump(table, f)
