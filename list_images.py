import os
import json
import requests

url = "https://api.digitalocean.com/v2/images?per_page=999"
headers = {"Authorization" : "Bearer " + os.environ['DIGITALOCEAN_ACCESS_TOKEN']}

r = requests.get(url, headers=headers)
distros = {}

for entry in r.json()["images"]:
    s = "(" + str(entry["id"]) + ") " + entry["name"]
    if entry["distribution"] in distros:
        distros[entry["distribution"]].append(s)
    else:
        distros[entry["distribution"]] = [s]

for key in distros:
    print key + ":"
    for list_elem in distros[key]:
        print "\t" + list_elem
