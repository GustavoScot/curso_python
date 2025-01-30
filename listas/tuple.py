# lista imutavel.
# lista de valores que tem sempre o mesmo numero de itens e nao pode ser modificada.
# Ordenada (pode acessar elementos pelo indice).

nomes = ('gustavo', 'pedro', 'nicholas')
# ou
nomes1 = tuple(('gabriel', 'julia', 'vitor'))

print(nomes,nomes1)

print(nomes[1])
print("-----------")

# contando quantas vezes algo se repete na lista
num = (1,2,3,4,4,4,5,6)
print(num.count(4))
print("-----------")

# a posicao do elemento
posicao_num = num.index(5)
print(posicao_num)
print("-----------")

# percorrendo a lista
for i in num:
    print(i)
print("-----------")

# mas pode percorrer pelo indice tambem
for x in range(0, len(num)):
    print(num[x])
print("-----------")

# alterando o tipo da lista
lista_tuple = (1,2,3)
lista_list = list(lista_tuple)
print(type(lista_list))
# agora podemos alterar a lista, pois agora ela é list
lista_list[1] = 5
lista_list.append('fim')
# agora que alterei, vou trocar para tuple novamente
lista_tuple = tuple(lista_list)
print(type(lista_tuple))
print(lista_tuple)

