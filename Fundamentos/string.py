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

texto4 = 'ola'
texto5 = ' TUDO certo?'
texto6 = ' muito bom '
modificado = texto4.upper() # deixa tudo maiusculo 
modificado2 = texto5.lower() # deixa tudo minusculo
modificado3 = texto6.title() # deixa a primeira letra das palavras em maiusculo
modificado4 = texto6.strip() # remove os espacos em branco em cada lado da string
modificado5 = texto6.rstrip() # remove os espacos em branco do lado direito da string
modificado6 = texto6.lstrip() # remove os espacos em branco do lado esquerdo da string
modificado7 = texto6.replace('bom', 'legal') # substitui a string

print(modificado)
print(modificado2)
print(modificado3)
print(modificado4)
print(modificado5)
print(modificado6)
print(modificado7)

