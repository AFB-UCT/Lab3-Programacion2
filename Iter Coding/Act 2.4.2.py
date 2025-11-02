# Crear un generador de numeros impares del 1 al 20 usando yield en una clase e iterarlo con un for


class Contador_Par:

    def __init__(self, inicio):
        self.actual=inicio
    
    def __iter__(self):
        for i in range(1, self.actual + 1):
            if i % 2 != 0:
                yield i



for num in Contador_Par(20):
    print(num)