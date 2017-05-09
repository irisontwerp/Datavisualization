import json
#
with open('setA_gemiddelewaterhardheid.json') as file1:
    dataSetA = json.load(file1)
with open('setB_latlon.json') as file2:
    dataSetB = json.load(file2)
    
print len(dataSetA)
print len(dataSetB)
