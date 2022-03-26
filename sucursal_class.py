from bodega_class import BodegaPrincipal

class Sucursal(BodegaPrincipal):
    def __init__(self, direccion, mt2, stock):
        super().__init__(direccion, mt2, stock)
        self.alarma = False

    def __str__(self):
        return f"Datos de sucursal:\n"'Dirección: {:<15} \nmts2: {:<15}'.format(self.direccion, self.mt2)

    def check():        #FUNCION PARA CORROBORAR EL ESTADO DE LA INSTANCIA(ALARMA)
        pass

    def despachar_producto(self, producto_elegido, cantidad, bodega): #Metodo sobrecargado
        if self.stock[producto_elegido]>=cantidad:
            print("Producto despachado a bodega")
            self.stock[producto_elegido]=self.stock[producto_elegido]-cantidad
            bodega.stock[producto_elegido]=bodega.stock[producto_elegido]+cantidad
            print(f"El nuevo stock es de {self.stock[producto_elegido]} unidad(es).")
        else: 
            print("Despacho rechazado, no hay suficiente stock")

    def recepcionar_producto(self, producto_elegido, cantidad):
        super().recepcionar_producto(producto_elegido, cantidad)
        if self.stock[producto_elegido]>500:
            self.stock[producto_elegido]=500

"""
sucursal=Sucursal("1 Norte 1400 Viña del Mar", 200,{"1":2,"2":20,"3":30, "4":2, "5":1} )
"""