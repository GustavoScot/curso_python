nome = 'Gustavo'
idade = 20
bio = ('Sou o %s e gosto de programar.' % (nome)) # %s para texto (string - str)
bio2 = ('Gosto de jogar bola e tenho %d anos.'% (idade)) # %d para numero inteiro (int)

situacao = True
faculdade = situacao 
print('Faz engenharia de software: %s' % (faculdade))

situacao = False
print('Ainda está na escola: %s' % (situacao))

dinheiro = 2.50
print('Tenho %.2f na conta. :(' % (dinheiro)) # %f para ponto flutuante (float)

print(bio)
print(bio2)
print('O nome dele é %s e tem %d anos'% (nome, idade))