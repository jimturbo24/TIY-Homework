import requests

testUrl = 'http://slpassist-dev.herokuapp.com/students'
resp = requests.get(testUrl)
data = resp.json()

# print(type(data))
print(data)

def crazyArgs(**kwarg):
    for (k, v) in kwargs.items():
        print(v)

crazyArgs(data)
