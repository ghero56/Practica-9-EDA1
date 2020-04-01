# Practica 9 ejercicio extra

#Triangulo
Triangulo_b = 2
Triangulo_h = 3

AreaT = (Triangulo_b * Triangulo_h)/2
PerimT = (10**(1/2)) + 2 + (10**(1/2))

print("El area del Triangulo es: ", AreaT, "El Perimetro del Triangulo es: ", PerimT)

#Circulo
PI = 3.1415
radio = 15

AreaC = radio**2 * PI
PerimC = PI * radio*2

print("El area del Circulo es: ", AreaC, "El Perimetro del Circulo es: ", PerimC)

#rectangulo
base = 10
altura = 15

AreaR = 10*15
PerimR = 10*2 + 15*2

print("El area del Rectangulo es: ", AreaR, "El Perimetro del Rectangulo es: ", PerimR)

#Trapecio
Bmayor = 10
Bmenor = 5
AlturaT = 3

PerimTra = Bmenor*3
PerimTra += (((Bmayor-Bmenor)**2)+(AlturaT**2))**(1/2)

AreaTra = AlturaT * (Bmayor + Bmenor)/2
PerimTra += Bmayor-Bmenor

print("El area del Trapecio es: ", AreaTra, "El Perimetro del Trapecio es: ", PerimTra)
