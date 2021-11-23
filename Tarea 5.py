#1
NUM1 = int(input("Ingresa un numero entero"))
NUM2 = int(input("Ingresa otro numero entero"))
if NUM1 == NUM2 :
    print(f"{NUM1} y {NUM2} son iguales")
else:
    if NUM1 > NUM2 :
        print( f"{NUM1} es el numero mayor y {NUM2} el numero  menor ")
    else:
        NUM1 < NUM2
        print(f"{NUM2} es el numero mayor y {NUM1} el numero  menor")
#2
num1 = int(input("Ingresa un numero entero"))
num2 = int(input("Ingresa otro numero entero"))
num3 = int(input("Ingresa otro numero entero"))
if num1 == num2 == num3 :
    print(f"Los valores son iguales")

elif num1 < num2 > num3:
    print(f"{num2} es el numero mayor")
elif num1 < num3 > num2: 
    print(f"{num3} es el numero mayor")
elif num2 < num1 >num3:
    print(f"{num1} es el numero mayor")
#3
num1 = int(input("Ingresa un numero entero"))
num2 = int(input("Ingresa otro numero entero"))
num3 = int(input("Ingresa otro numero entero"))
if num1 == num2 == num3 :
    print(f"Los valores son iguales")

elif num1 > num2 < num3:
    print(f"{num2} es el numero menor")
elif num1 >num3 < num2: 
    print(f"{num3} es el numero menor")
elif num2 > num1< num3:
    print(f"{num1} es el numero menor")
#4
num1 = int(input("Ingresa un numero entero"))
num2 = int(input("Ingresa otro numero entero"))
num3 = int(input("Ingresa otro numero entero"))
num4 = int(input("Ingresa otro numero entero"))

if(num1 > num2 and num1 > num3 and num1 > num4):
 a= num1
else:
 if(num2 > num1 and num2 > num3 and num2 > num4):
  a= num2
 else:
  if(num3 > num1 and num3 > num2 and num3 > num4):
   a=num3
  else:
   a=num4
if(num1 < num2 and num1 < num3 and num1 < num4):
 b=num1
else:
 if(num2 < num1 and num2 < num3 and num2 < num4):
  b= num2
 else:
  if(num3 < num1 and num3 < num2 and num3 < num4):
   b= num3
  else:
   b=num4
print("el  numero mayor es "+str(a)+" y el numero menor es "+str(b))
