import requests

url = 'http://127.0.0.1:8000/api/persona/'


# crear persona
def crear():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")

    data = {
        "name": nombre,
        "last_name": apellido,
        "edad": edad
    }
    r = requests.post(url, auth=('admin', 'Admin2023*'), data = data)
    
    code = r.status_code
    # data = r.json()
    
    print("Code: ", str(code))
    # print("Data: ", data)

# Listar persona
def listar():
    r = requests.get(url, auth=('admin', 'Admin2023*'))

    code = r.status_code
    data = r.json()
    
    print("Code: ", str(code))
    
    for d in data:
        print(d)

# actualizar persona
def actualizar():
    id = input("Id persona a actualizar: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")

    print(url + id + "/")

    data = {
        "name": nombre,
        "last_name": apellido, 
        "edad": edad
    }
    r = requests.patch(url + id + "/", auth=('admin', 'Admin2023*'), data = data)
    
    code = r.status_code
    # data = r.json()
    
    print("Code: ", str(code))
    # print("Data: ", data)

# eliminar persona
def eliminar():
    id = input("Id persona a eliminar: ")

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