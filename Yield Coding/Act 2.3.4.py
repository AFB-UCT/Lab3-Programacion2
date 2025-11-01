# Crear una Funcion Generadora que genere la serie de fibonacci hasta el decimo elemento usando yield 


# para la funcion de Fibonacci empieza con los numeros a=0 y b=1
def Fibonacci(n):
    a, b = 0, 1
    # Por la cantidad de veces que coloces en el n, en este caso 10
    for n in range(n):
        # Me almacenaras y guardaras el resultado esperado (1, 1 ,2 , 3, 5...)
        yield b
        # Seguido de eso ese resultado almacenado se sumara con otro termino conformado por si mismo y editara y almacenara ese nuevo termino a la A 
        # De esta forma seguira dando diferentes resultados con diferentes datos almacenados hasta que cumpla el range(n)
        a, b = b, a + b



for numero in Fibonacci(10):
    print(numero)