from pprint import pprint
import requests
from config import URL


r = requests.get(URL)

kurslar = r.json()

for kurs in kurslar:
    pprint(kurs['code'])

