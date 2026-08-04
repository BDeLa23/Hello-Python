name, surname, age = "Pepe", "Juan", 35   # Asignamos el nombre, el apellido y la edad a las variables.

# Mostramos el contenido de las variables utilizando distintos métodos de formateo.

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))  # * Explicación al final
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # Esta es la opción que más os recomiendo, es muy simple.

'''
*
%s = String = "hola", 'hola' 
%d = Número entero = 1
%f = Número decimal 1.5
'''