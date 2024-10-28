import requests

api_key = '04bd7138-9ffb-4ec5-9397-1c1e794a7784'
word = ' hallo'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()
print(definitions)

for definition in definitions:
    print(definition)