import requests as r

API_URL = 'https://coji-code.com'

resp = r.get(f'{API_URL}/coji-code/get/kmfkkmlfdkafcgfd')
print(resp)
print(resp.json())