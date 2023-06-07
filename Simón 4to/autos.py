#Herencia
class Auto:#CLASE AUTO
    def init(self,nom,mod,color,precio):#CONSTRUIR CLASE PADRE
        self.nom=nom
        self.mod=mod
        self.color=color
        self.precio=precio
    def descripcion(self):
        print(f"Nombre:{self.nom} Modelo:{self.mod} Color:{self.color} Precio{self.precio}")
class Chevrolet(Auto):
    def init(self,nom,mod,color,precio,marca):
        super().init(nom,mod,color,precio)
        self.marca=marca
    def descripcion(self):
        super().descripcion()
        print(f"Marca{self.marca}")

a1=Auto("Versa",2021,"Negro","15000")
a1.descripcion()
a2=Chevrolet("Aveo",2022,"Rojo",1000000,"Chevrolet")
a2.descripcion()
a3=Chevrolet("Onix",2022,"Negro",140000,"Chevrolet")
a3.descripcion()