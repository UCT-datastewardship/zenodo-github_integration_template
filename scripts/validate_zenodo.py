import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
zenodo_file = '.zenodo.json'
schema_file = 'zenodo_schema.json'
try:
    with open(zenodo_file, 'r') as f:
        zenodo_data = json.load(f)
except FileNotFoundError:
    print(f'Error: {zenodo_file} not found.')
    exit(1)
except json.JSONDecodeError as e:
    print(f'Error: {zenodo_file} is not valid JSON:')
    print(e)
    exit(1)
try:
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    validate(instance=zenodo_data, schema=schema)
    print(f'{zenodo_file} is valid against the Zenodo schema.')
except ValidationError as e:
    print(f'Error: {zenodo_file} does not conform to the Zenodo schema:')
    print(e)
    exit(1)
except FileNotFoundError:
    print(f'Error: Schema file {schema_file} not found.')
    exit(1)
except json.JSONDecodeError as e:
    print(f'Error: Schema file {schema_file} is not valid JSON:')
    print(e)
    exit(1)
