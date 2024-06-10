import json
import re
data = []
def load_words_json():
    with open("lexical.json", 'r') as f:
        data = json.load(f)
    return data

# data = load_words_json()
# print(data)

f = open("lexical.json", "r")
print(f.read())

