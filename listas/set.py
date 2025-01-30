#Nao ordenado e sem elementos duplicados.
#Pode adicionar elementos, mas nao modificar elementos existentes.
#Nao é possivel acessar elementos pelo indice.

lista_set = {}
#ou
lista1_set = set({})

set1 = {1,2,3}
print(set1)

#pode adicionar ou remover
set1.add(5)
print(set1)
set1.remove(1)
print(set1)
print("-----------")

#nao aceita valores duplicados
lista = {1,2,3,3,4,4}
print(lista)
print("-----------")

#limpando a lista
lista.clear()
print(lista)
print("-----------")

#percorrendo a lista
lista = {1,2,3,False, 5.5, 'oi'}
for i in lista:
    print(i)
print("-----------")

#unindo listas
lista2 = {1,2,3,4,5}
lista3 = {4,5,6,7}
lista_unida = lista2.union(lista3)
print(lista_unida)
print("-----------")

#intercessao das listas
lista2 = {1,2,3,4,5}
lista3 = {4,5,6,7}
lista_inter = lista2.intersection(lista3)
print(lista_inter)
print("-----------")

#a diferenca das listas
lista2 = {1,2,3,4,5}
lista3 = {4,5,6,7}
lista_dif = lista2.difference(lista3)
lista_dif2 = lista3.difference(lista2)
print(lista_dif)
print(lista_dif2)
print("-----------")

