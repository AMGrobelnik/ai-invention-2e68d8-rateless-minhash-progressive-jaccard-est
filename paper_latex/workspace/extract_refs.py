import re
import json

# Build references list based on the bibliography provided in paper_text
refs = [
    {"doi": "10.1145/2594538.2594554", "author": "Pagh", "year": 2014, "title": "Is min-wise hashing optimal for summarizing set intersection?"},
    {"doi": "10.1145/2566486.2568017", "author": "Mitzenmacher", "year": 2014, "title": "Efficient estimation for high similarities using odd sketches"},
    {"doi": "10.1109/tkde.2020.3021176", "author": "Ertl", "year": 2019, "title": "ProbMinHash -- A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity"},
    {"doi": "10.1109/TIT.2002.1009229", "author": "Luby", "year": 2002, "title": "LT codes"},
    {"doi": "10.1109/TIT.2006.874390", "author": "Shokrollahi", "year": 2006, "title": "Raptor codes"},
    {"doi": "10.14778/3457390.3457394", "author": "Ertl", "year": 2021, "title": "SetSketch: Filling the Gap between MinHash and HyperLogLog"},
    {"doi": "10.1145/2488388.2488463", "author": "Li", "year": 2014, "title": "One Permutation MinHash"},
    {"doi": "10.1145/3097983.3098058", "author": "Shrivastava", "year": 2017, "title": "Densified One Permutation MinHash"},
    {"doi": "10.1109/ICDM.2010.80", "author": "Ioffe", "year": 2010, "title": "Improved consistent sampling, weighted minhash and L1 sketching"},
]

print("References to fetch:")
print(json.dumps(refs, indent=2))
