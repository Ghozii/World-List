import requests

api_key = 'be0c44e2-ddcd-42ea-a579-24feec43fa4c'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)