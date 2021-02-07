'''
while True:
    if terra:
        passo
    if espaco:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega
'''

'''
cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('fim')
'''

'''
cont = 1
while True:
    print(cont, '...', end='')
    cont += 1
    if cont == 10:
        break
print('fim')
'''

'''
n = s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
print(f'a soma é: {s}')
'''

########## DESAFIO 66 ###########
'''
soma = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    soma += n
print(f'a soma é: {soma}')
'''

########## DESAFIO 67 ###########
'''
while True:
    n = int(input('digite um numero para mostrar a tabuada: '))
    if n < 0:
        print('o numero é negativo, o programa sera interrompido')
        break
    else:
        for c in range(1, 11):
            print(f'{n}x{c} = {n*c}')
'''

########## DESAFIO 68 ##########
'''
from random import randint
win = 0
while True:
    j = int(input('digite um numero: '))
    r = randint(0, 11)
    print(f'para testes, o numero digitado pela maquina: {r}')
    soma = j + r
    o = str(input('digite o que voce quer(par ou impar): '))
    if o == 'par':
        if soma%2 == 0:
            print('voce ganhou')
            win += 1
        else:
            print('voce perdeu, o programa fechara')
            break
    elif o == 'impar':
        if soma%2 == 1:
            print('voce ganhou')
            win += 1
        else:
            print('voce perdeu, o programa fechara')
            break
print(f'o numero de vezes que voce ganhou foi: {win}')
'''

########## DESAFIO 69 ###########
'''
qtdi = 0
qtdh = 0
qtdm = 0
while True:
    i = int(input('digite sua idade: '))
    s = str(input('digite seu sexo: ')).upper().strip()[0]
    while s not in 'MF':
        s = str(input('digite seu sexo: ')).upper().strip()[0]
    if i >= 18:
        qtdi += 1
    if s == 'M':
        qtdh += 1
    if s == 'F' and i < 20:
        qtdm += 1

    o = str(input('quer continuar? [s/n] ')).upper().strip()[0]
    while o not in 'SN':
        o = str(input('quer continuar? [s/n] ')).upper().strip()[0]
    if o == 'N':
        break
print(f'a quantidade de pessoas maiores que 18 anos é: {qtdi}')
print(f'a quantidade de homens é: {qtdh}')
print(f'a quantidade de mulheres com menos de 20 anos é: {qtdm}')
'''

########## DESAFIO 70 ##########
'''
total = 0
menor = 0
cont = 0
qtd = 0
barato = ''
while True:
    n = str(input('digite o nome do produto: '))
    p = float(input('digite o preco do produto: '))
    cont += 1
    total += p
    if p > 1000:
        qtd += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n
    o = str(input('quer continuar? [s/n] ')).strip().upper()[0]
    while o not in 'SN':
        o = str(input('quer continuar? [s/n] ')).strip().upper()[0]
    if o == 'N':
        break
print(f'o total foi: {total}')
print(f'a qtd de produtos q custam mais de 1000R é: {qtd}')
print(f'o produto mais barato é: {barato}')
'''

########## DESAFIO 71 ##########
valor = int(input('qual o valor do saque? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de R${ced}')
        elif ced ==  50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break