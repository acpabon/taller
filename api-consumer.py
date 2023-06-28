import requests

url = 'http://127.0.0.1:8000/api/mascotas/'


# crear mascotas
def crear():
    nombre = input("Nombre mascota: ")

    data = {
        "name": nombre,
        "owner": 1
    }
    r = requests.post(url, auth=('admin', 'Admin2023*'), data = data)
    
    code = r.status_code
    # data = r.json()
    
    print("Code: ", str(code))
    # print("Data: ", data)

# Listar mascotas
def listar():
    r = requests.get(url, auth=('admin', 'Admin2023*'))

    code = r.status_code
    data = r.json()
    
    print("Code: ", str(code))
    
    for d in data:
        print(d)

# actualizar mascotas
def actualizar():
    id = input("Id mascota a actualizar: ")
    nombre = input("Nombre mascota: ")

    print(url + id + "/")

    data = {
        "name": nombre
    }
    r = requests.patch(url + id + "/", auth=('admin', 'Admin2023*'), data = data)
    
    code = r.status_code
    # data = r.json()
    
    print("Code: ", str(code))
    # print("Data: ", data)

# eliminar mascotas
def eliminar():
    id = input("Id mascota a eliminar: ")

    r = requests.delete(url + id + "/", auth=('admin', 'Admin2023*'))
    
    code = r.status_code
    # data = r.json()
    
    print("Code: ", str(code))
    # print("Data: ", data)


opcion = input("Elija una opción: \n 1 - listar\n 2 - crear \n 3 - actualizar \n 4 - eliminar \n")

if opcion == '1':
    listar()
elif opcion == '2':
    crear()
    listar()
elif opcion == '3':
    actualizar()
    listar()
elif opcion == '4':
    eliminar()
    listar()
else:
    print("Elija una opción valida")