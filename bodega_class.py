class BodegaPrincipal:
    
    def __init__(self, direccion, mt2, stock):
        self.direccion= direccion
        self.mt2=mt2
        self.stock=stock

    def despachar_producto(self, producto_elegido, cantidad, sucursal):
        if self.stock[producto_elegido]>=cantidad:
            print("Producto despachado a sucursal")
            self.stock[producto_elegido]=self.stock[producto_elegido]-cantidad
            sucursal.stock[producto_elegido]=sucursal.stock[producto_elegido]+cantidad
            print(f"El nuevo stock es de {self.stock[producto_elegido]} unidad(es).")
        else: 
            print("Despacho rechazado, no hay suficiente stock")

    def recepcionar_producto(self, producto_elegido, cantidad):
            self.stock[producto_elegido]=self.stock[producto_elegido]+cantidad
            print("Producto recepcionado")

    def __str__(self):
        return f"Datos Bodega principal:\n"'Dirección: {:<15} \nmts2: {:<15}'.format(self.direccion, self.mt2)

    def mostrar_stock(self):
        for key in self.stock:
            print(key, self.stock[key])

"""
b={"1":100,"2":100,"3":100, "4":100, "5":100}
a=Bodega_principal("Arlegui 400 Viña del Mar", 500, b)

"""