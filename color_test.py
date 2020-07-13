import sys
import pip._vendor.requests
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("Jai"))

r = requests.get("https://google.com")
print(r.status_code)
