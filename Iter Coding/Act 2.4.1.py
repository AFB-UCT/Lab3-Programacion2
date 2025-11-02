# Crear un contador del 10 al 15 usando iter() y recorrerlo con next()

# Creo una clase contador que contiene lo siguiente
class Contador:
    # El Init, que solamente recibira el numero con el que quieres
    # Comenzar, en este caso 10, pero tambien tendra el limite 15 (self.fin)

    def __init__(self, inicio):
        self.actual=inicio
        self.fin=15
    # Sigo sin entender como funciona el __iter__ en este ejemplo, Sera un ancla
    def __iter__(self):
        return self
    # esta es la funcion para que el ciclo continue hasta que 
    # este llegue al self.fin osea 15.
    def __next__(self):
        if self.actual <= self.fin:
            valor=self.actual
            self.actual+=1
            return valor
        else:
            raise StopIteration
        
for num in Contador(10):
    print(num)