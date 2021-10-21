nombre= "Angel"
edad= 18
casado = False
estatura= 1.75

print( nombre,edad,casado,estatura ) 
print("nombre:"+ nombre +"\n\tedad:" + str(edad) + "\n\testa casado:"+ str(casado))

print(nombre + "" + str(edad) + "" + str(casado) + "" + str(estatura) )

print("nombre {3}\n\tedad: {2}\n\testa casado: {1}\n\testatura en metros:{0}".format(nombre,edad,casado,estatura))

print("Con el operador f\"\"")

print(f"nombre {nombre}\n\tedad: {edad}\n\testa casado: {casado}\n\testatura en metros:{0}")

print(f"Hola {nombre}")
