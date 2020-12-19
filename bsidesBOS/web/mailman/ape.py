import requests

url = "http://challenge.ctf.games:30814/"

data = {
    "name": "test",
    "email": "user.agenta@gmail.com",
    "message": "test"
}

response = requests.post(url, data)
print(response.text)