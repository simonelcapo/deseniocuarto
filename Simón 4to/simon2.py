class Producto:
    def _init_(self,idprod,stock, nombre, precio,idprov):
       self.idprod = idprod
       self.stock = stock
       self.nombre = nombre
       self.precio = precio
       self.idprov = idprov

    def mostrar(self):
        print("codigo producto:",self.idprod)
        print("nombre del producto:",self.nombre)
        print("stock: ",self.stock)
        print("precio:",self.precio)
        print("codigo del proveedor:",self.idprov)
while True:
    op = int(input("menu:\n 1)agregar un producto \n 2)mostrar producto\n 3)salir"))
    if op == 2:
        objeto=input("ingrese nombre del producto:")
        ip = int(input("ingrese el codigo del producto:"))
        nom = input("ingrese el nombre del producto:")
        s = int(input("ingrese stock:"))
        p=float(input("ingrese precio"))
        iprov =int(input("ingrese el codigo del proveedor"))
        objeto = Producto(ip,nom,s,p,iprov)
    elif op == 2:
        objeto.mostrar()
    elif op == 3:
        print("cerrando el sistema >:)")
        break