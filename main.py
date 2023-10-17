class Cliente:
    def __init__(self, name, lastname, email, address, age, username, password):
        self.name = name
        self.age = age
        self.lastname = lastname  
        self.email = email
        self.address = address
        self.cart = []
        self.username = username  
        self.password = password

        

    def __str__(self):
        return f"name: {self.name} {self.lastname}, age: {self.age}, email: {self.email}, address: {self.address}"

#funciones que las paso al "test"

#agregar al carrito

    def addcart(self, producto, cantidad, precio):
        if producto in cosas:
            self.cart.append({"producto": producto, "cantidad": cantidad, "precio": precio})
            print(f"{cantidad} {producto} agregado al carrito de  {self.name} {self.lastname}")
        else:
            print(f"{producto} error")


# mostrar el carrito

    def showcart(self):
        if not self.cart:
            print(f"el carrito ta vacio")
        else:
            print(f"carrito de  {self.name} {self.lastname}:")
        total = 0  
        for producto in self.cart:
            cantidad = producto["cantidad"]
            precio = producto["precio"]
            subtotal = cantidad * precio  
            total += subtotal  
            print(f"{cantidad} {producto['producto']} x {precio} = {subtotal}")
        print(f"Total del carrito: {total}")

#limpiar el carrito 

    def cleancart(self, producto):
        for item in self.cart:
            if item["producto"] == producto:
                self.cart.remove(item)
            print(f"{producto} eliminado del carrito de {self.name} {self.lastname}")
            return  
        print(f"{producto} no se encontró en el carrito de {self.name} {self.lastname}")


    def login(self, username , password):
        if self.username == username and self.password == password:
            print(f"Bienvenido {self.name}")
        else:
            print("Nombre de usuario o contraseña incorrectos")

cosas = {
     
     "computadora" : 100,
     "telefono" : 200 
}  
 

