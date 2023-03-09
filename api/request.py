import requests
import time
import json
import sys

if(not len(sys.argv) == 2 or sys.argv[1] not in {'CNN', 'SVM', 'RF'}):
    print("\nUsage: python request.py [SVM|CNN|RF]\n")
    exit(1)

algo = sys.argv[1]
## PYTHON API
t = time.time()
for i in range(500):
    response = requests.post('http://127.0.0.1:5000/predict', json={"algo": algo, "transaction": [10, 265803.35, 0.00, 0.00, 751669.39, 1017472.74, 0, 1, 0, 0, 0, 0 ]})
t = time.time() - t

print("\nPython time: " + str(round(t,2)) + " s")

message = json.loads(response.content.decode('utf-8'))
print(message)

## JAVA API
t = time.time()
for i in range(500):
    response = requests.post('http://127.0.0.1:8080/predict', json={"algo": algo, "transaction": [10, 265803.35, 0.00, 0.00, 751669.39, 1017472.74, 0, 1, 0, 0, 0, 0 ]})
t = time.time() - t

print("\nJAVA time: " + str(round(t,2)) + " s")

message = json.loads(response.content.decode('utf-8'))
print(message)

