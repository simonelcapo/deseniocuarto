class persona:
    def _init_(self,nombre,dni,edad,direccion):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.direccion=direccion
    def descripcion(self):
        print(f"nombre: {self.nombre} edad: {self.edad} dni: {self.dni} direccion: {self.direccion}")

p1=persona("Juan Alvarez", 23456789, "a")