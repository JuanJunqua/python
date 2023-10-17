from main import *

users = {}
def register():
    user = input("usuario?: ")
    password = input("password?: ")
    name = input("nombre?")
    lastname = input("apellido?")
    email = input("email?: ")
    address = input("direccion?: ")
    age = int(input("edad?: "))
    
    if user not in users:
        users[user] = Cliente(name, lastname, email, address, age, user, password)
        print("usuario registrado")
    else:
        print("el usuario ya esta registrado.")




def login():
    user = input("usuario: ").lower()  
    password = input("password: ")

    if user in users and users[user].password == password:
        print("Welcome!")
        return users[user]
    else:
        print("Usuario o passwrod incorrectos.")
        return None


while True:
    action = input(" registrarse (1) iniciar sesion (2) ")
    if action.lower() == '1':
        register()
    elif action.lower() == '2':
        current_client = login()
        if current_client:
            break




# ***Agregar al carrito ***
producto = input("Producto (computadora o telefono): ")
cantidad = int(input("Cantidad: "))
precio = float(input("Precio: "))

current_client.addcart(producto, cantidad, precio)

# ***Mostrar carrito ***
mostrarcarrito = input(" mostrar el carrito? (si/no): ")
if mostrarcarrito.lower() == "si":
    current_client.showcart()

# ***Limpiar carrito ***
eliminar = input("modificar carrito ? (si/no): ")
if eliminar.lower() == "si":
    delete = input("cual? ")
    current_client.cleancart(delete)

