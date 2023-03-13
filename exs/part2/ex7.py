import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
meth = "get"

print(f'{requests.get(url).status_code} - {requests.get(url).text} - for GET method without params')
print(f'{requests.head(url).status_code} - {requests.head(url, data={"method": "HEAD"}).text} for GET method with params HEAD')
print(f'{requests.post(url).status_code} - {requests.post(url, data={"method": "POST"}).text}- for POST method with params POST')
print("---------------------------GET---------------------------")

while meth == "get":
    methResponse = requests.get(url, params={"method": "GET"})
    print(f'{methResponse.status_code} - {methResponse.text} - for GET method with params GET')
    methResponse = requests.get(url, params={"method": "POST"})
    print(f'{methResponse.status_code} - {methResponse.text} - for GET method with params POST')
    methResponse = requests.get(url, params={"method": "PUT"})
    print(f'{methResponse.status_code} - {methResponse.text} - for GET method with params PUT')
    methResponse = requests.get(url, params={"method": "DELETE"})
    print(f'{methResponse.status_code} - {methResponse.text} - for GET method with params DELETE')
    print("---------------------------POST---------------------------")
    meth = "post"
while meth == "post":
    methResponse = requests.post(url, data={"method": "GET"})
    print(f'{methResponse.status_code} - {methResponse.text} - for POST method with params GET')
    methResponse = requests.post(url, data={"method": "POST"})
    print(f'{methResponse.status_code} - {methResponse.text} - for POST method with params POST')
    methResponse = requests.post(url, data={"method": "PUT"})
    print(f'{methResponse.status_code} - {methResponse.text} - for POST method with params PUT')
    methResponse = requests.post(url, data={"method": "DELETE"})
    print(f'{methResponse.status_code} - {methResponse.text} - for POST method with params DELETE')
    print("---------------------------PUT---------------------------")
    meth = "put"
while meth == "put":
    methResponse = requests.put(url, data={"method": "GET"})
    print(f'{methResponse.status_code} - {methResponse.text} - for PUT method with params GET')
    methResponse = requests.put(url, data={"method": "POST"})
    print(f'{methResponse.status_code} - {methResponse.text} - for PUT method with params POST')
    methResponse = requests.put(url, data={"method": "PUT"})
    print(f'{methResponse.status_code} - {methResponse.text} - for PUT method with params PUT')
    methResponse = requests.put(url, data={"method": "DELETE"})
    print(f'{methResponse.status_code} - {methResponse.text} - for PUT method with params DELETE')
    print("---------------------------DELETE---------------------------")
    meth = "delete"
while meth == "delete":
    methResponse = requests.delete(url, data={"method": "GET"})
    print(f'{methResponse.status_code} - {methResponse.text} - for DELETE method with params GET')
    methResponse = requests.delete(url, data={"method": "POST"})
    print(f'{methResponse.status_code} - {methResponse.text} - for DELETE method with params POST')
    methResponse = requests.delete(url, data={"method": "PUT"})
    print(f'{methResponse.status_code} - {methResponse.text} - for DELETE method with params PUT')
    methResponse = requests.delete(url, data={"method": "DELETE"})
    print(f'{methResponse.status_code} - {methResponse.text} - for DELETE method with params DELETE')
    print("---------------------------------------------------------")
    meth = "stop"
else:
    print("DONE")

