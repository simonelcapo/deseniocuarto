class producto: 
    def __init__(self,nombre,precio,canstock,idproveedor):
        self.nombre = nombre 
        self.precio = precio 
        self.canstock = canstock 
        self.idproveedor = idproveedor
        def mostrar (self):
            print("producto:", self.nombre) 
            print("precio:", self.precio)

p1=producto("CocaCola, 180, 10, Distribuidora 5 A 1")
p1.mostrar()