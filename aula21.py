'''
def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela
    :param i: inicio
    :param f: final
    :param p: passo
    :return: nao tem
    """
    while i <= f:
        print(f'{i} ', end=' ')
        i += p
    print('fim')


contador(2, 10, 2)
help(contador)
'''

'''
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'a soma é: {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
'''

'''
def teste():
    x = 8
    n = 4
    print(f'na fincao, x vale {x}')
    print(f'na funcao, n vale {n}')


# MAIN
n = 2
print(f'no programa principal, n vale {n}')
teste()
'''

'''
def teste():
    global n
    x = 8
    n = 4
    print(f'na fincao, x vale {x}')
    print(f'na funcao, n vale {n}')


# MAIN
n = 2
print(f'no programa principal, n vale {n}')
teste()
print(f'no programa principal, n vale {n}')
'''

'''
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


resp = somar(3, 2, 5)
print(resp)
# OU #
print(somar(3, 2, 5))

print('os resultados foram: ')
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(r1, r2, r3)
'''

'''
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('digite um numero: '))
print(f'o fatorial de {n} é {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados foram {f1}, {f2}, {f3}')
'''

'''
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('digite um numero: '))
if par(num):
    print('é par')
else:
    print('nao é par')
'''

######### DESAFIO 101 ##########
'''
def voto(idade):
    if idade >= 18:
        return 0
    if idade >= 16 and idade <=17:
        return 1
    else:
        return 2


# MAIN
idade = int(input('digite sua idade: '))
if voto(idade) == 0:
    print('seu voto é obrigatorio!')
if voto(idade) == 1:
    print('seu voto é opcional!')
if voto(idade) == 2:
    print('voce nao pode votar!')
'''

########## DESAFIO 102 ##########
'''
def fatorial(num, show = False):
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ', end='')
        fat = fat * c
    print(fat)


# MAIN
x = int(input('digite um numero: '))
print('o fatorial do numero escolhido é: ')
fatorial(x, show = True)
'''

########## DESAFIO 103 ##########
'''
def ficha(nome = '<desconhecido>', gol = 0):
    print(f'o jogador {nome} fez {gol} gols no camp')


nome = str(input('Nome do jogador: '))
gol = str(input('Numero de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    g = 0
if nome.strip() == '':
    ficha(gol = g)
else:
    ficha(nome, gol)
'''

########## DESAFIO 104 ##########
'''
def leiaint(frase):
    ok = False
    valor = 0
    while True:
        n = str(input(frase))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Numero invalido!')
        if ok:
            break
    return valor


#MAIN
n = leiaint('digite um numero: ')
print(f'voce digitou o numero {n}')
'''

########## DESAFIO 105 ###########
'''
def notas(*num, sit = False):
    dici = dict()
    dici['total'] = len(num)
    dici['maior'] = max(num)
    dici['menor'] = min(num)
    dici['media'] = sum(num) / len(num)

    if sit:
        if dici['media'] >= 7:
            dici['sit'] = 'Boa'
        elif dici['media'] >= 5:
            dici['sit'] = 'Mais ou menos'
        else:
            dici['sit'] = 'Ruim'

    return dici

# MAIN
main = notas(10, 15, 20, 30, 45, sit = True)
print(main)
'''

########## DESAFIO 106 (incompleto) ##########
'''
c = ('\033[m', # 0 - sem cores
    '/'
    )

def ajuda(com):
    help(com)


def titulo(msg, cor = 0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


comando = ''
while True:
    titulo('sistema de ajuda pyhelp')
    comando = str(input('Funcao ou Biblioteca: '))
    if comando.upper() == 'Fim':
        break
    else:
        ajuda(comando)
titulo('Ate Logo!')
'''