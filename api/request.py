import requests
import time
import json
import sys

algo = sys.argv[1]
## PYTHON API
t = time.time()
for i in range(100):
    response = requests.post('http://127.0.0.1:5000/predict', json={"algo": algo, "transaction": [10, 265803.35, 0.00, 0.00, 751669.39, 1017472.74, 0, 1, 0, 0, 0, 0 ]})
t = time.time() - t

print("Python time: " + str(t))

message = json.loads(response.content.decode('utf-8'))
print(message)

## JAVA API
t = time.time()
for i in range(100):
    response = requests.post('http://127.0.0.1:8080/predict', json={"algo": algo, "transaction": [10, 265803.35, 0.00, 0.00, 751669.39, 1017472.74, 0, 1, 0, 0, 0, 0 ]})
t = time.time() - t

print("JAVA time: " + str(t))

message = json.loads(response.content.decode('utf-8'))
print(message)

