# Crear una clase que genere los cuadrados de los numeros del 1 al 10 sin usar Iter(). pero proporcionando un metodo que devuelva la lista completa

class Cuadrados:
    def __init__(self,n):
        self.n=n

    def obtener_lista(self):
        resultado=[]
        for i in range(1, self.n+1):
            resultado.append(i**2)
        return resultado
    
for c in Cuadrados(10).obtener_lista():
    print(c)