from urllib.request import urlopen
import json

with urlopen('https://api.ipify.org?format=json') as response:
    # response.read() returns type bytes
    # Use decode('utf-8') to decode bytes to text, so that json loads could work on it.
    print(json.loads(response.read().decode('utf-8'))['ip'])