import requests


url = 'http://127.0.0.1:8000/api/mascotas/'

r = requests.get(url)
code = r.status_code
print('mascotas - code', code)

data = r.json()
print('mascotas - data', data)


url = 'http://127.0.0.1:8000/api/observacion/'

r = requests.get(url)
code = r.status_code
print('observacion - code', code)

data = r.json()
print('observacion - data', data)