from utils import read_json
import json

'''
This file contains all the configuration for the API.
It will read the configuration from pyjson.config.json file.
Then use this syntax as the template to convert PyJSON code to Python code.
'''

filename = 'pyjson.config.json'
pyjson_data: dict = read_json(filename)
dumped_pyjson_data: str = json.dumps(pyjson_data)

KEYWORDS = pyjson_data['KEYWORDS']
START_KEYWORDS = pyjson_data['START_KEYWORDS']
END_KEYWORDS = pyjson_data['END_KEYWORDS']

GENERAL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS
}

# Keywords for calculation and comparison
VAR_KEYWORDS = pyjson_data['VAR_KEYWORDS']
CALC_KEYWORDS = {
    **VAR_KEYWORDS,
}

# Keywords for handling blocks
BLOCK_KEYWORDS = pyjson_data['BLOCK_KEYWORDS']

ALL_KEYWORDS = {
    **GENERAL_KEYWORDS,
    **CALC_KEYWORDS,
    **BLOCK_KEYWORDS
}

RESPONSE_TEMPLATE = {
    'status': 'success',
    'stdout': '',
    'stderr': ''
}
if __name__ == '__main__':
    print(KEYWORDS['print'] % 'Hello World')
