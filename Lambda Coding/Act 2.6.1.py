# Crear una funcion lambda que reciba dos numeros y devuelva el mayor
# basicamente lambda recive las cantidades de 1 y 666, para verifiar si 1 es menor que 666 y dar un resultado booleano (True/False).
# Podria hacer un metodo con imputs para que sea mas interactivo, pero creo que esta es la forma mas sencilla para exponer la problematica.

Mayor=lambda x, y : x < y

print(Mayor(1,666))