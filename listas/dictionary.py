# Lista com chave/valor.
# Permite modificacoes, mas nao permite valores duplicados para as chaves.
# A chave e o valor podem ser de qualquer tipo.

idades = {
#   chave : valor
    'ana' : 10,
    'joao' : 20,
    'bia' : 30.6,
    'vini' : 'indefinido'}

print(idades)
print(idades['ana'])
print("-----------")

# atualizando a lista
idades['bia'] = 31 # alterando o valor
idades['carlos'] = 70 # adicionando na lista
idades.pop('vini') # tirei 'joao' da lista
print(idades)
idades.popitem() # tirei o ultimo da lista
print(idades)
print("-----------")

# convertendo para tuple
lista = idades.items()
print(lista, end='\n\n')
for item in lista:
    print(item[0], item[1])
print("-----------")

# separar a chave dos valores
chaves = idades.keys()
valores = idades.values()
for item in chaves:
    print(item)
print("")
for item in valores:
    print(item)
print("-----------")

# contar quantas vezes se repete
idades_novas = {'pepe': 20, 'jota': 40, 'lua': 20}
lista_nome = list(idades_novas.values())
idade_20 = lista_nome.count(20)
print(idade_20)
print("-----------")

# limpar a lista
idades.clear()
print(idades)
print("-----------")

# dictionary dentro de dictionary
dados_ana = {
    'sexo' : 'feminino',
    'cpf' : '123456789',
    'rg' : '6647832'
}
dados_livia = {
    'sexo' : 'feminino',
    'cpf' : '987654321',
    'rg' : '48376437'
}
dados_rafa = {
    'sexo' : 'masculino',
    'cpf' : '657483921',
    'rg' : '7859432'
}

todos_dados = {
    'ana' : dados_ana,
    'livia' : dados_livia,
    'rafa' : dados_rafa
}

print(todos_dados)
print(todos_dados['ana']['sexo'])
print(todos_dados['rafa']['rg'])
print("-----------")

#  ou
dados_juntos = {
    'helena' : {
        'sexo' : 'feminino',
        'cpf' : '019847385',
        'rg' : '1235321'
    },

    'juliana' : {
        'sexo' : 'feminino',
        'cpf' : '8376589392',
        'rg' : '4674367'
    },

    'nich' : {
        'sexo' : 'masculino',
        'cpf' : '843784832',
        'rg' : '89767478'
    }
}

print(dados_juntos)
print(dados_juntos['juliana']['rg'])
print(dados_juntos['nich']['sexo'])