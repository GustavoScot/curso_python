for x in range(10):  # de 0 a 9 (coloquei apenas o limite)
    print(x)

print('----------')

for x in range(5, 10):  # de 5 a 9 (coloquei onde comeca e onde termina)
    print(x)

print('----------')

for x in range(5, 20, 5):  # de 5 a 20 mas de 5 em 5 (coloquei onde comeca, onde termina e o step)
    print(x)

print('----------')

for x in range(20, 4, -2): # comeca em 20 e termina em 4 (de 2 em 2) 
    print(x) 

print('----------')

texto = 'gustavo'
for x in range(0, len(texto)):
    print(texto[x])

print('----------')

nome= "vitor"
for i in nome:
    print(i)

print('----------')

letra = input('Digite uma letra: ')

if (len(letra) != 1):
    print('Apenas 1 digito.')
else:
    texto1= input('Digite uma palavra: ')

    for i in range(0, len(texto1)): #verificando se tem a letra no texto1
        if letra == texto1[i]:
            print('Encontrei a letra %s na posicao %d'% (letra, i))

print('----------')

for x in range(1,5): # tabuada do 1 ate o 5
    for y in range(1,11):
        multiplicacao = x * y
        print('%d x %d = %d' % (x, y, multiplicacao))