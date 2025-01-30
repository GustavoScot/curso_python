numero = 10

while(numero > 0): # enquanto o numero for maior que 0
    print(numero)
    numero -= 1 # esta diminuindo o numero

print("acabou.")

numero2= 0

while (numero2 < 5):
    print(numero2)
    numero2 += 1 # esta aumentando o numero

print('fim.')

texto = "ola gente"
        #012345678
indice = 0

while(indice < len(texto)): # enquanto o indice for menor que a quantidade de caracteres do texto
    print(texto[indice]) # imprimir o texto que esta na posicao do indice 
    indice += 1 # esta aumentando o indice 
print('acabou.')

numero3= 1

while (True):
    if numero3 == 6:
        break
    print(numero3)
    numero3 += 1 

print('fim.')

numero4 = 0
while (numero4 < 10):
    numero4 += 1
    if numero4 % 2 == 0:
        continue # pulou os numeros pares
    print(numero4)
print('fim.')
