import json
import sys
sys.path.insert(0, '/ai-inventor/.claude/skills/aii-semscholar-bib/scripts')
from aii_semscholar_bib__fetch import core_semscholar_bib_fetch

references = [
    {"doi": "10.1145/2594538.2594554", "author": "Pagh", "year": 2014},
    {"doi": "10.1145/2566486.2568017", "author": "Mitzenmacher", "year": 2014},
    {"doi": "10.1109/tkde.2020.3021176", "author": "Ertl", "year": 2019},
    {"doi": "10.1109/TIT.2002.1009229", "author": "Luby", "year": 2002},
    {"doi": "10.1109/TIT.2006.874390", "author": "Shokrollahi", "year": 2006},
    {"doi": "10.14778/3457390.3457394", "author": "Ertl", "year": 2021},
    {"doi": "10.1145/2488388.2488463", "author": "Li", "year": 2014},
    {"doi": "10.1145/3097983.3098058", "author": "Shrivastava", "year": 2017},
    {"doi": "10.1109/ICDM.2010.80", "author": "Ioffe", "year": 2010},
]

result = core_semscholar_bib_fetch(references)
print(json.dumps(result, indent=2))
