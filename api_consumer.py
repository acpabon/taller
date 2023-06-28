import requests


url = 'http://127.0.0.1:8000/api/mascotas/'

# GET  -- listar
r = requests.get(url)
code = r.status_code
print('mascotas - code', code)

data = r.json()
print('mascotas - data', data)

# POST  -- Crear
payload = {
    "name": "mascota 4",
    "owner": 1
}
r = requests.post(url, data=payload)
code = r.status_code
print('mascotas - create - code', code)


r = requests.get(url)
code = r.status_code
print('mascotas - code', code)

data = r.json()
print('mascotas - data', data)



## Observations

url = 'http://127.0.0.1:8000/api/observacion/'

r = requests.get(url, auth=('admin', 'admin'))
code = r.status_code
print('observacion - code', code)

data = r.json()
print('observacion - data', data)