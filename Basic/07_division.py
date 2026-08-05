# División

language = "Python"

language_slice = language[1:3] # Imprimimos los caracteres a partir del 1 hasta el 3
print(language_slice)

language_slice = language[1:] # Imprimimos los caracteres a partir del 1 hasta el final
print(language_slice)

language_slice = language[-2] # Imprimimos el carácter -2 (se cuenta por el final)
print(language_slice)

language_slice = language[1:5:2] # Imprimimos los caracteres a partir del 1 hasta el 5 con un salto de 2 carácteres
print(language_slice)

'''
El patrón que usa es:
inicio:final:salto
el salto predeterminado el valor es 1. (si lo dejas vacío)

inicio: desde dónde empezar (si se omite, empieza al principio).
final: hasta dónde llegar (si se omite, llega hasta el final).
salto: cuánto avanza en cada salto.
'''