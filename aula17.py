'''
lanche = ['hamb', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picole'
print(lanche)
#a lista pode ser modificada

lanche.append('cookie') #adciona no final
print(lanche)

lanche.insert(0, 'hot dog')
print(lanche)
lanche.insert(2, 'agua')
print(lanche)
#adiciona em qualquer lugar

del lanche[3]
print(lanche)
lanche.remove('hamb')
print(lanche)
lanche.pop(1)#com o indice remove o ultimo, sem remove o indice
print(lanche)

if 'hamb' in lanche:
    lanche.remove('hamb')#sem o if dará erro
    print(lanche)
'''

'''
#valores = list(range(4, 11))
#print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse = True)
print(valores)
len(valores)
print(f'o tamanho é {len(valores)}')
'''

'''
num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('nao achei o 4')
print(num)
print(f'essa lista tem {len(num)} elementos')
'''

'''
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor: {v}')
print('cheguei no final da lista')
'''

'''
a = [2, 3, 4, 7]
b = a[:]#ele apenas cria uma copia, nao cria ligacao
b[2] = 8
print(f'a lista A: {a}')
print(f'a lista B: {b}')
'''

######### DESAFIO 78 #########
'''
lista = []
for cont in range(0, 5):
    lista.append(int(input('digite um numero: ')))
me = ma = lista[0]
for c in lista:
    if c > ma:
        ma = c
    if me > c:
        me = c
print(f'o maior valor é {ma} e o menor é {me}')
'''

########## DESAFIO 79 ##########
'''
lista = list()
while True:
    n = int(input('digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('o valor ja existe')
    o = str(input('quer continuar? [s/n]'))
    if o in 'Nn':
        break
print(lista)
'''

######### DESAFIO 80 ##########
'''
lista = []
for c in range (0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
'''

######### DESAFIO 81 ##########
'''
lista = []
while True:
    lista.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar? '))
    if resp in 'Nn':
        break
print(lista)
print(f'foram digitados {len(lista)} numeros')
lista.sort(reverse = True)
print(lista)
if 5 in lista:
    print('tem 5 na lista')
else:
    print('o 5 nao ta lista')
'''

########## DESAFIO 82 ##########
'''
lista = []
par = []
impar = []
while True:
    lista.append(int(input('digite um numerO: ')))
    o = str(input('quer continuar? [s/n]'))
    if o in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(lista)
print(par)
print(impar)
'''

########## DESAFIO 83 ##########
expr = str(input('digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressao esta valida')
else:
    print('sua expressao esta errada')