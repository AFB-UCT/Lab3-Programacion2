#Crear una funcion generadora que reciba una lista de numeros y devuelva los numeros impares usando yield

#Creare el mismo generador que cree en el ejercicio anterior
def contador(lista):
    for i in lista:
        #aun que las diferencias empiezan aqui, ya que el i tomara solamente los elementos que no sean pares (resto 2)
        if i % 2 != 0:
            yield i

#Creo la Lista...
ListaNum=[1,2,3,4,5,6,7,8,9,10]

for num in contador(ListaNum):
    #y como resultado la terminal tendria que imprimir 1,3,5,7 y 9
    print(num)