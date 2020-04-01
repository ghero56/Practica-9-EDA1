#practica 9 (python)

#--------variables y tipos----------#
x = 10 # variable x con valor entero de 10
print(x) # imprimimos el valor de x

cadena = 'Hola Mundo' # variable cadena con tipo cadena
print(cadena)

x = y = z = 10 # se asigna el mismo valor a 3 variables
print(x,"\t",y,"\t",z) # se imprimen los 3 valores separados por comas ','

type(x) # funcion type recibe una variable la cual retorna su tipo
type(cadena)

x = "Hola Mundo" # al cambiar el tipo de la variable no hay que castear
cadena = 10 # simplemente es automatico

SEGUNDOS_POR_DIA = 60*60*24
PI = 3.14

#--------cadenas----------#
cadena1 = 'Hola'
cadena2 = "Mundo"
print(cadena1)
print(cadena2)
concat_cadenas = cadena1 + cadena2 # se concatenan cadenas con el operador +
print(concat_cadenas)

num_cadena = str(cadena) + ' ' + concat_cadenas # se concatenan variables de diferentes tipos conviertiendolas en cadena
print(num_cadena) # se imprime el resultado

num_cadena = "{} {} {}".format(cadena1, cadena2, cadena) # el operador {} sirve para imprimir variables segun el orden que recibe format
print(num_cadena) # todas ya en formato cadena

num_cadena = 'Cambiando el orden: {1} {2} {0}'.format(cadena1, cadena2, cadena)
print(num_cadena)

#--------operadores----------#
#aritmeticos ( +, *, -, /, %, ** )
print(1+5)
print(6*3)
print(10-4)
print(100/50)
print(10%2)
print(((20*3)+(10+1))/10)
print(2**3)

#booleanos (and,or,not)
False and True

#comparación ( <, >, <=, >=, ==, !=)
print(7 < 5)
print(7 > 5)
print((11*3)+2 == 36 + 1)
print((11*3)+2 >= 36)
print("curso"!='CuRsO')

#--------Listas----------#

#--------Tuplas----------#

#--------Tuplas con nombre----------#

#--------Diccionarios----------#

#--------Funciones----------#

#--------Variables Globales----------#
