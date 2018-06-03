import json
import pprint
from pathlib import Path


module_name = 'crop_yield_delphi.json'
filename = (Path(__file__).parents[0]/'..'/'..'/'data'/'program_analysis'/module_name).resolve()

print(filename)

with open(filename) as f:
    data = json.load(f)

print('DELPHI_JSON:')
pprint.pprint(data)