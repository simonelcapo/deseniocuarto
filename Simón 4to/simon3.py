class Producto:
    def _init_(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
    def mostrar (self):
        print("nombre de producto:",self.nombre, "precio de producto:",self.precio)
    def vender (self):
        cantidad= int(input("cuanto quiere comprar:"))
        subtotal= cantidad*self.precio
        print("el total es:",subtotal)
        total=subtotal+total
        print("total",total)

p1= Producto("metanfetaminas",550)
p2= Producto("ketasis",550)
p3= Producto("crack",550)
p4= Producto("marihuana",2100)
p5= Producto("cocaina",400)
p6= Producto("sales de baño",250)

while True:
    menu=input("")
    if menu=="1":
        p1.mostrar()
        p1.vender()
    elif  menu=="2":
        p2.mostrar()
        p2.vender()
    elif  menu=="3":
        p3.mostrar()
        p3.vender()
    elif  menu=="4":
        p4.mostrar()
        p4.vender()
    elif  menu=="5":
        p5.mostrar()
        p5.vender()
    elif  menu=="6":
        p6.mostrar()
        p6.vender()
    break