import requests
import random

looping = True

while looping:

    slumpnr = random.randint(1, 30000)

    url =f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={slumpnr}&_limit=1"

    req = requests.get(url)
    json_data = req.json()
    list_results = json_data["results"]
    personnummer = list_results[0]['testpersonnummer']


    print(personnummer[2: 12])

    svar = input("\nvill ni slumpa ett personnummer till? j/n\n")

    if (svar == "n"):
        break