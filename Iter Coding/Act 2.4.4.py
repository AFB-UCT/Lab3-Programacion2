# Crear un iterador que recorra los elementos de una lista de cadenas y devuelva cada cadena en mayusculas
# p.upper()
# mayusculas=list(map(lambda p: p.upper, liista)) ?

class Mayusculas:
    def __init__(self,lista):
        self.lista=lista
        self.lista=[]

    def __iter__(self, lista):
        mayusculas=[]
        mayusculas.append=list(map(lambda p: p.upper, self.lista))


listaC=["hola","wenas","como","estan"]

for Cadena in Mayusculas(listaC):
    print(Cadena)