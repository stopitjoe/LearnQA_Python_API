import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
firstResponse = response.history[0]
secondResponse = response.history[1]
redirectCounts = str(len(response.history))

print("1. " + str(firstResponse.status_code) + " - " + str(firstResponse.url))
print("2. " + str(secondResponse.status_code) + " - " + str(secondResponse.url))
print('Redirect count: ' + redirectCounts)
