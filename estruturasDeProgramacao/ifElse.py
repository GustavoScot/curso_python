valor1= 10
valor2= 10
sao_iguais= (valor1 == valor2)
if sao_iguais:
    print("sao iguais 1")

valor3= 20
valor4= 20
if (valor3 == valor4): print("sao iguais 2")  

if (valor1 != valor3): print("sao diferentes 1")  

if (valor3 != valor4): print("sao diferentes 2")  
else: print("sao iguais 3")

print ("-----------")

numero = 11
if numero % 2 == 0: 
    print("numero par")
else: 
    print("numero impar")    

numero2 = 9
if numero2 > 0 and numero2 < 10:
    print("menor que 10 ")
else:
    print ("maior que 10")

print ("-----------")

numero3 = 5
if numero3 < 10:
    print("menor que 10")
    if numero3 > 0:
        print("positivo")
    else: print("negativo")

elif numero3 < 100:
    print("menor que 100")

elif numero3 < 1000:
    print("menor que 1000")

else:
    print("maior que 1000")

print("----------")    

numero4 = 2
resultado = "Um" if numero4 == 1 else "Dois" if numero4 == 2 else "tres"
print(resultado) 
print("----------")    
