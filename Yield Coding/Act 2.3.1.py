# Crear una funcion generafora que devuelva los primeros 10 numeros pares usando yield y recorrerla con un for
# Nota: Crear Repo GH
#Defino una funcion "contador"
def contador(n):
    #por el numero que coloquemos en "n", en el ciclo for de abajo
    for i in range(n):
            #Tomara cada numero par y seguira hasta que este termine el recorrido cuando llegue al numero 10
            #el i+=1 es para que empieze por el 1 y a si mismo me incluya el 10 en este recorrido
            i += 1
            if i % 2 == 0: 
                yield i

#Entonces, por los numeros en el contador N=10, vas a imprimirme cada numero que salga de la funcion del contador (osea, cada numero que es PAR)
for numeros in contador(10):
    print(numeros)