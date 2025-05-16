import requests
schema_url = 'https://raw.githubusercontent.com/zenodo/zenodo/master/zenodo/modules/deposit/jsonschemas/deposits/records/legacyrecord.json'
response = requests.get(schema_url)
response.raise_for_status()  # Raise an exception for bad status codes
with open('zenodo_schema.json', 'w') as f:
    f.write(response.text)
