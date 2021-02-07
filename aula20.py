'''
def mostralinha():
    print('-' * 30)


mostralinha()
print('       Sistema de Alunos:         ')
mostralinha()
'''

'''
def mensagem(msg): #com parametro
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('      Sistemas de Alunos')
mensagem('PEDRO')
'''

'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

# COM FUNCOES #

def soma(x1, x2):
    s = x1 + x2
    print(s)

# MAIN
soma(4, 5)
soma(9, 8)
soma(2, 1) 
'''

'''
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    tam = len(num)
    print(f'tem {tam} numeros')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos += 1

valores = [7, 2, 5, 0, 5]
print(f'os valores normais sao: {valores}')
dobra(valores)
print(f'os valores dobrados sao: {valores}')
'''

'''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'a soma eh: {s}')


soma(5, 2)
soma(5, 2, 4, 6)
'''

########## DESAFIO 96 ##########
'''
def arearet():
    b = int(input('digite a base: '))
    h = int(input('digite a altura: '))
    a = b * h
    print(f'a area é: {a}')


arearet()
'''

########## DESAFIO 97 ##########
'''
def escreva(txt):
    print('~' * 30)
    print(txt)
    print('~' * 30)


escreva('pedro')
escreva('dalton pikas')
'''

########## DESAFIO 98 ##########
'''
def contador(i, f, p):
    print(f'contara de {i} ate {f} de {p} em {p}')

    if i < f:
        while i <= f:
            print(f'{i} ', end='')
            i += p
    else:
        while i >= f:
            print(f'{i}', end='')
            i -= p


# MAIN

contador(1, 10, 1)
print('\n')
contador(10, 0, 2)
print('\n')

ini = int(input('digite o valor do inicio: '))
fim = int(input('digite o valor do fim: '))
passo = int(input('digite o valor que ira pulando: '))
contador(ini, fim, passo)
'''

########## DESAFIO 99 ##########
'''
def maior(*num):
    cont = 0
    ma = 0
    for c in num:
        print(f'{c} ', end='')
        if c == 0:
            ma = c
        else:
            if c > ma:
                ma = c
        cont += 1
    print(f'foram diitados {cont} numeros')
    print(f'o maior valor informado foi: {ma}')


# MAIN
maior(2, 9, 7, 4, 8)
'''

########## DESAFIO 100 ##########
'''
from random import randint
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'a soma dos pares é: {soma}')


# MAIN
numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)
'''
