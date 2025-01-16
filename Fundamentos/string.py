texto1 = 'oi'
texto2 = ','
texto3 = ' tudo bem?'
print(texto1 + texto2 + texto3 )

repeticao = texto1 * 3
print(repeticao)

nome = input('Nome: ')
idade = input('Idade: ')
idade = int(idade) 
print('Meu nome e %s e tenho %d anos.' % (nome, idade))

texto = 'vitor'
verificacao = 'i' in texto # tem 'i' no texto? 
verificacao2 = 'g' in texto 
verificacao3 = 'vit' in texto 
print(verificacao) 
print(verificacao2)
print(verificacao3)

tamanho = len(texto) # quantos caracteres tem no texto
tamanho2 = len(texto1)
print(tamanho)
print(tamanho2)