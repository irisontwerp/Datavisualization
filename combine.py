import json

output_file = 'combined_data.json'
setA_file = 'setA.json'
setB_file = 'setB.json'

def load_set(set_file):
    with open(set_file, 'rt') as f:
        return json.load(f)


def get_hardness(gemeente):
    for entry in setA:
        if entry['Gemeente '] == gemeente:
            return entry['Gemiddelde waterhardheid']


# Load the sets into memory
setA = load_set(setA_file)
setB = load_set(setB_file)
setC = []

# Add data from set b to set c and append the water hardness for 
# that community
for entry in setB:
    c_entry = entry
    gemeente = entry[' gemeente'].replace("'", '')
    c_entry['Gemiddelde waterhardheid'] = get_hardness(gemeente)
    setC.append(c_entry)

# Dump the json to a file
with open(output_file, 'wt') as f:
    json.dump(setC, f)
