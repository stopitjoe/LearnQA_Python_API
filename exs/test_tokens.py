import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
newResponse = requests.get(url)
newObj = newResponse.json()
token = newObj['token']
oldResponse = requests.get(url, params={"token": {token}})
oldObj = oldResponse.json()

print(f'status - {oldObj["status"]}')
print(f'Waiting {newObj["seconds"]} seconds...')
time.sleep(newObj["seconds"])

oldResponse = requests.get(url, params={"token": {token}})
oldObj = oldResponse.json()

print(f'status - {oldObj["status"]}')
print(f'result is {oldObj["result"]}')