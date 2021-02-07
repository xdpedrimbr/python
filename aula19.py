'''
dados = {}
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'#cria o elemento sexo e coloca o M, tipo o append
del dados['idade']
print(dados)
'''

'''
filme = {'titulo': 'star wars',
         'ano': 1977,
         'diretor': 'george lucas'
         }

filme1 = {'titulo': 'avengers',
         'ano': 2012,
         'diretor': 'joss'
         }

filme2 = {'titulo': 'matrix',
         'ano': 1999,
         'diretor': 'wachowski'
         }

print(filme.values())#printa so os valores, sem as keys
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'o {k} é {v}')

locadora = [filme, filme1, filme2]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
'''

'''
pessoas = {'nome': 'pedro', 'sexo': 'M', 'idade': 18}
print(pessoas['nome']) #o elemento é um nome
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #mostra as tuplas

pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''
brasil = []
estado1 = {'uf': 'minas gerais', 'sigla': 'mg'}
estado2 = {'uf': 'sao paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')
'''

########## DESAFIO 90 ##########
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    print('voce foi aprovado')
else:
    print('voce foi reprovado')
'''

########## DESAFIO 91 ##########
'''
from random import randint
from time import sleep
from operator import itemgetter
player = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6), }
rank = list()
print('foi sorteado os valores: ')
for k, v in player.items():
    print(f'{k} tirou {v} no dado')

rank = sorted(player.items(), key=itemgetter(1), reverse = True)
print(rank)

for i, v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
'''

########## DESAFIO 92 ##########
'''
ctps = dict()
ctps['nome'] = str(input('digite o nome: '))
ctps['ano'] = int(input('digite o ano de nascimento: '))
ctps['carteira'] = int(input('digite o numero da carteira de trabalho: '))

idade = 2019 - ctps['ano']
apos = idade + 35

if ctps['carteira'] != 0:
    ctps['contratacao'] = int(input('digite o ano que voce foi contratado: '))
    ctps['salario'] = int(input('digite seu salario: '))
    print(f'o nome é: {ctps["nome"]} \na idade é: {idade} \na carteira de trabalho é: {ctps["carteira"]}')
    print(f'o ano que voce foi contratado: {ctps["contratacao"]} \no seu salario é: {ctps["salario"]} \nvoce se aposentara com {apos} anos')
else:
    print(f'o nome é: {ctps["nome"]} \na idade é: {idade} \na carteira de trabalho é: {ctps["carteira"]}')
    print('Fim do programa, voce nao trablha ainda')
'''

########## DESAFIO 93 ##########
'''
aprov = dict()
gol = list()
totgol = 0
aprov['nome'] = str(input('digite o nome do jogador: '))
aprov['part'] = int(input('digite a quantidade de partidas que ele jogou: '))

for c in range(1, aprov['part']+1):
    gol.append(int(input(f'quantos gols ele fez na partida {c}: ')))

for t in gol:
    totgol += t

aprov['gols'] = gol
aprov['total de gols'] = totgol

print(f'o nome do jogador é: {aprov["nome"]}; \nos gols nas respectivas partidas foram: {aprov["gols"]}; '
      f'\no total de gols foram: {aprov["total de gols"]}')

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

print(f'o jogador {aprov["nome"]} jogou {len(aprov["gols"])} partidas')
for i, v in enumerate(aprov['gols']):
    print(f'na partida {i} fez {v} gols')
'''

########## DESAFIO 94 ##########
'''
dici = {}
lista = []
qtd = 0
soma = 0
media = 0

while True:
    dici.clear()
    dici['nome'] = str(input('Nome: '))
    while True:
        dici['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if dici['sexo'] in 'MF':
            break
        print('digite um sexo valido!!')
    dici['idade'] = int(input('Idade: '))
    soma = dici['idade'] + soma
    lista.append(dici.copy())
    while True:
        o = str(input('quer continuar? [S/N]')).upper()[0]
        if o in 'SN':
            break
        print('digite uma opcao valida!!')
    if o == 'N':
        break
print(f'ao todo temos {len(lista)} pessoas registradas')
media = soma / len(lista)
print(f'a media é: {media}')
print(lista)
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ')
print('pessoa acima da media: ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
'''

########## DESAFIO 95 (BUGADO) ###########

time = list()
aprov = dict()
gol = list()
totgol = 0

while True:
    aprov.clear()
    aprov['nome'] = str(input('digite o nome do jogador: '))
    aprov['part'] = int(input('digite a quantidade de partidas que ele jogou: '))
    

    for c in range(1, aprov['part']+1):
        gol.append(int(input(f'quantos gols ele fez na partida {c}: ')))

    for t in gol:
        totgol += t

    aprov['gols'] = gol
    aprov['total de gols'] = totgol
    time.append(aprov.copy())

    while True:
        o = str(input('quer continuar? [s/n]')).upper()[0]
        if o in 'SN':
            break
        print('opcao invalida, digite apenas s ou n!!')
    if o in 'Nn':
        break

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d)}:<15', end='')
    print()

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

print(f'o jogador {aprov["nome"]} jogou {len(aprov["gols"])} partidas')
for i, v in enumerate(aprov['gols']):
    print(f'na partida {i} fez {v} gols')







