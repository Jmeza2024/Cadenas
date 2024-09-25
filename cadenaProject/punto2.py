# -*- coding: utf-8 -*-

# Solicitar al usuario su nombre completo
full_name = raw_input("Por favor, introduce tu nombre completo: ")

# Contar el número de letras excluyendo los espacios
num_letters = len(full_name.replace(" ", ""))

# Saludar al usuario e informarle la longitud de su nombre
print("Hola, {}! Tu nombre tiene {} letras, excluyendo los espacios.".format(full_name, num_letters))
