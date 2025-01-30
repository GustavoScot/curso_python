# Vetores dinamicos (pode alterar ela a qualquer momento). 
# Pode ser modificado com adicao e remocao. 
# ordenada (pode acessar elementos pelo indice).

array = []
# ou
array = list()

array_num = [1 ,2 ,3]
#posicao =   0, 1, 2
array_float = [1.5, 2.4, 50.5, 2.2, 3.5]
array_str = ["A", "B", "C"]
array_misto = [5, 6.5, "D", False]
print(array)
print(array_num)
print(array_float)
print(array_str)
print(array_misto)
print("-----------")

print(array_num[0])
print(array_float[1])
print(array_str[2])
print(array_misto[0])
print("-----------")

array_num[2] = 4
print(array_num)
print("-----------")

print(array_num[-1])     
print("-----------")

print(array_float[1 : 4])
print("-----------")

# inserir valor ao final da lista
array_num.append(5)
print(array_num)

# inserir na posicao do indice
array_num.insert(2, 3) #inserindo na posicao 2 o numero 3
print(array_num)
print("-----------")

# removendo valores
array_num.remove(1) # removendo por valor
print(array_num)
array_num.pop(1) # removendo pela posicao 
print(array_num)
print("-----------")

# limpar a lista
array_str.clear()
print(array_str)
print("-----------")

# verificando se tem na lista
print(4 in array_num)
print(2.7 in array_float)
print(True in array_misto)
print("-----------")

# verificando quantas vezes algo se repete
lista = [1,2,3,1,5,3,1]
print(lista.count(1))
print("-----------")

# qual posicao esta o indice
pos = lista.index(5)
print(pos)
print("-----------")

# juntando listas
array1 = [1,2,3]
array2 = [3,4,5]
print(array1 + array2)
print("-----------")

# multiplicando a lista
multi = array1 * 3
print(multi)
print("-----------")

# unpacking
x,y,z = array1
print(x)
print(y)
print(z)
_,a,b = array2
print(a)
print(b)
print("-----------")

# percorrer a lista
nomes = ['gustavo', 'vitor', 'pedro']
for i in nomes:
    print(i)
print("-----------")

# lista dentro da lista
listas = [[1,2,3], [4,5,6]]
primeira_lista = listas[0]
segunda_lista = listas[1]
print(primeira_lista)
print(segunda_lista)

primeira_lista_valores = listas[0][1]
segunda_lista_valores = listas[1][2]
print(primeira_lista_valores)
print(segunda_lista_valores)
