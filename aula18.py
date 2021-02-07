'''
dados = list()
dados.append('pedro')
dados.append(25)
print(dados)

pessoas = list()
pessoas.append(dados[:])
pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
print(pessoas[0][0]) #dentro do 0 vai printar o 0
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
'''

'''
teste = list()
teste.append('pedro')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
'''

'''
galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade]')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores')
'''

########## DESAFIO 84 ##########
'''
geral = list()
nep = list()
qtd = 0
ma = me = 0
while True:
    nep.append(str(input('digite o nome: ')))
    nep.append(int(input('digite o peso: ')))
    if len(geral) == 0:
        ma = me = nep[1]
    else:
        if nep[1] > ma:
            ma = nep[1]
        if nep[1] < me:
            me = nep[1]
    geral.append(nep[:])
    nep.clear()
    qtd += 1
    o = str(input('quer continuar o cadastro? [s/n] '))
    if o in 'Nn':
        break


print(f'a quantidade de pessoas cadastradas é: {qtd}')
print(f'a pessoa mais pesada é {ma} e a mais leve é {me}')
'''

########## DESAFIO 85 ##########
'''
lista = [[], []]
for c in range(1, 8):
    n = int(input(f'digite o {c} valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'a lista é: {lista}')
lista[0].sort()
lista[1].sort()
print(f'Par: {lista[0]}')
print(f'impar: {lista[1]}')
'''

########## DESAFIO 86 ##########
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #1º, 2º e 3º linha
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}][{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
'''

########## DESAFIO 87 ###########
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacol = 0
somalin = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}][{coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]

for linha in range(0, 3):
    somacol += matriz[linha][2]

for coluna in range(0, 3):
    somalin += matriz[1][coluna]

print(f'a soma dos pares é: {somapar}')
print(f'a soma dos elementos da 3 coluna é: {somacol}')
print(f'a soma dos elementos da 2 coluna é: {somalin}')
'''

########## DESAFIO 88 ##########
'''
from random import randint
total = 1
sorteados = []
lista = []
jogos = int(input('quantos jogos voce quer? '))
while total <= jogos:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorteados.append(lista[:])
    lista.clear()
    total += 1
print(f'os numeros sorteados foram: {sorteados}')
'''

########## DESAFIO 89 ##########
ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = int(input('nota1: '))
    nota2 = int(input('nota2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('quer continuar? '))
    if resp in 'Nn':
        break
print(ficha)