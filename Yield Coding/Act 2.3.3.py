# Crea Una Clase con un metodo __iter__() que use yield para generar los cuadrados de los numeros del 1 al 10
# Nota: Buscar Explicar Esto.

class Cuadrado:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        
        for i in range(1, self.n + 1):
            yield i**2
        
for c in Cuadrado(10):
    print(c)