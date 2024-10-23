import json
data= {}

def JsonSerialize(data, sFile):
    with open(sFile, 'w') as write_file:
        json.dump(data, write_file)