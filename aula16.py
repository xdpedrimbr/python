#print(lanche[0:2])
#print(lanche[1:])
#print(lanche[-1])
#len(lanche)
# for c in lanche:  #a variavel c so aceita uma comida
#     print(c) #printa cada comida dentro de lanche
##### nao é possivel mudar uma tupla(vetor) #####

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[0:2])
print(lanche[-2])
print(lanche[1:])
print(lanche[1:3])
print(lanche[:2])
print(lanche[0:-1])
#lanche[1] = 'refrigerante' #imutavel
#print(lanche[1])
print('############################################################')
for comida in lanche:
    print(f'eu vou comer: {comida}')
print('to de buchim chei')
print('###########################################################')
for cont in range(0, len(lanche)):
    print(f'eu comi: {lanche[cont]}')
print('comi pra krl')
print('############################################################')
for cont in range(0, len(lanche)):
    print(f'vou comer {lanche[cont]} na posicao {cont+1}')
print('pronto')
print('##############################################################')
for pos, comida1 in enumerate(lanche):
    print(f'eu vou comer {comida1} na posicao {pos+1}')
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim','batata frita')
print(lanche)
print(sorted(lanche)) #ordenada
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(a)
print(b)
print(c)
print(f'a lista ordenada é: {sorted(c)}')
print(f'o tamnaho é: {len(c)}')
print(f'esta aparecendo {c.count(5)} vezes o numero 5')
print(f'o 8 aparece na posicao {c.index(8)}')

del(a)#deleta a tupla
'''

########### DESAFIO 72 ##########
'''
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('digite o numero desejado: '))
print(f'o numero {n} por extenso é: {numeros[n]}')
'''

########## DESAFIO 73 ##########
'''
tabela = ('jpedro0', 'wpedro1', 'apedro2', 'hpedro3', 'opedro4', 'kpedro5', 'pedro6', 'bpedro7', 'jpedro8', 'gpedro9', 'fpedro10', 'tpedro11', 'kpedro12', 'bpedro13', 'vpedro14', 'mpedro15', 'npedro16', 'zpedro17', 'apedro18', 'gpedro19', 'hpedro20')
print(f'os 5 primeiros colocados sao: {tabela[0:5]}')
print(f'os 4 ultimos colocados sao: {tabela[-4:]}')
print(f'a lista em ordem alfabetica é: {sorted(tabela)}')
print(f'a posicao q se encontra o kpedro5 é: {tabela.index(kpedro5)}')
'''

########### DESAFIO 74 ##########
'''
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'a tupla é: {n}')
s = sorted(n)
print(f'o menor valor é {s[0]} e o maior é {s[-1]}') #pode usar o max(n) e min(n)
'''

########## DESAFIO 75 ##########
'''
n = (int(input('digite um numero da tupla ')), int(input('digite um numero da tupla ')), int(input('digite um numero da tupla ')), int(input('digite um numero da tupla ')))
print(f'a tupla é: {n}')
print(f'o valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'a posicao do primeiro numero 3 é {n.index(3)}')
else:
    print('nao apareceu nenhum numer 3')
for c in n:
    if c % 2 == 0:
        print(f'o {c} é par')
'''

########## DESAFIO 76 ##########
'''
itens = ('lapis', 1.75,
         'borracha', 2,
         'caderno', 15.90,
         'estojo', 25,
         'mochila', 120,
         'caneta', 22.35,
         'livro', 34.89)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7}')
'''

########### DESAFIO 77 ###########
'''
n = ('pedro', 'dalton', 'pikas', 'escola', 'rua', 'henrique')
print(f'a lista de palavras é: {n}')
for c in n:
    print(f'na palavra {c} tem a vogal: ')
    for letra in c:
       if letra.lower() in 'aeiou':
           print(letra)
'''



