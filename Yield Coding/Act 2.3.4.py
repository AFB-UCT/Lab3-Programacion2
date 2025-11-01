# Crear una Funcion Generadora que genere la serie de fibonacci hasta el decimo elemento usando yield 
#resultados esperados: 1,1,2,3,5,8,12,21,34,55
# F(n)= F(n-1) + F(n-2)
# Y si hago un producto con n-1, otro con n-2 y luego los sumo?

def Fibonacci(n):
    for i in range(n):
        i += 0
        if Fibonacci(i-1) + Fibonacci(i-2):
            yield i



for f in Fibonacci(10):
    print(f)