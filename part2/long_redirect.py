import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
firstResponse = response.history[0]
secondResponse = response.history[1]

print(firstResponse.status_code)
print(firstResponse.url)
print(secondResponse.status_code)
print(secondResponse.url)
