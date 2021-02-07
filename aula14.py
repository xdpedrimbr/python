'''
while not maca:
    passo
pega
'''

'''
while not maca:
    if terra:
        passo
    if espaco:
        pula
pega
'''

'''
c = 1
while c <= 10:
    print(c)
    c = c + 1
print('fim while')

##para for:
for c in range(1,11):
    print(c)
print('fim for')
'''

'''
r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('quer continuar? [s/n]: ')).upper()
'''

'''
qtdimpar = 0
qtdpar = 0
n = 1
while n != 0:
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        qtdpar = qtdpar + 1
    else:
        qtdimpar = qtdimpar + 1
print('digtou 0, portanto pare')
print('a quantidade de par é {} e a de impar é {}'.format(qtdpar, qtdimpar))
'''

######### DESAFIO 57 ##########
'''
sexo = str(input('informe seu sexo [m/f]: '))
while sexo not in 'MmFf':
    sexo = str(input('digite novamente: '))
print('sexo {} deu certo'.format(sexo))
'''

########## DESAFIO 58 ###########
'''
import random
pc = random.randint(0, 10)
print('apenas para testes: {}'.format(pc))
acertou = False
while not acertou:
    usu = int(input('digite um numero entre 0 e 5: '))
    if pc == usu:
        print('voce acertou o numero sorteado')
        acertou = True
    else:
        print('voce digitou o numero errado')
'''

########## DESAFIO 59 ##########
'''
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
opcao = 0

while opcao != 5:
    opcao = int(input('digite a opcao desejada: '
                  '\n1-soma'
                  '\n2-multiplica'
                  '\n3-maior'
                  '\n4-novos numeros'
                  '\n5-sair do programa'))

    if opcao == 1:
        soma = n1 + n2
        print('a soma é: {}'.format(soma))
    elif opcao == 2:
        multi = n1 * n2
        print('a multiplicacao é: {}'.format(multi))
    elif opcao == 3:
        if n1 > n2:
            print('o maior é: {}'.format(n1))
        else:
            print('o maior é: {}'.format(n2))
    elif opcao == 4:
        n1 = n3 = int(input('digite o primeiro numero: '))
        n2 = n3 = int(input('digite o segundo numero: '))
    elif opcao == 5:
        print('programa finalizado com sucesso!')
    else:
        print('opcao invalida, tente novamente')
    print('*********************************************************************************')
'''

'''
########## DESAFIO 60 ##########
n = int(input('digite um numero: '))
f = n
fat = 1
while f > 0:
    print('{}'.format(f), end='')
    print(' x ' if f > 1 else ' = ', end='')
    fat = fat * f
    f = f - 1
print(fat)
'''

########### DESAFIO 61 ##########
'''
p1 = int(input('digite o primeiro numero: '))
r = int(input('digite a razao da PA: '))
print('o 1º termo é: {}'.format(p1))
cont = 2
while cont < 10:
    p1 = p1 + r
    cont += 1
    print('o {}º termo é: {}'.format(cont, p1))
#for c in range(2, 11):
#    p1 = p1 + r
#    print('o {}º termo é: {}'.format(c, p1))
'''
########### DESAFIO 62 ###########
'''
p1 = int(input('digite o primeiro numero: '))
r = int(input('digite a razao da PA: '))
print('o 1º termo é: {}'.format(p1))
cont = 1
while cont < 10:
    p1 = p1 + r
    cont += 1
    print('o {}º termo é: {}'.format(cont, p1))

opcao = str(input(('quer mostrar mais termos? [S/N] ')))
cont2 = 10

if opcao == 's':
    add = int(input('digite a quantidade para adcionar: '))
    add2 = add + 10
    while cont2 >= 10 and cont2 < add2:
        p1 = p1 + r
        cont2 += 1
        print('o {}º termo é: {}'.format(cont2, p1))

    if add == 0:
        print('o programa nao pode adicionar 0')
else:
    print('entao é isso')
'''

########## DESAFIO 63 ##########
'''
n = int(input('digite ate onde a sequencia vai: '))
n1 = 0
n2 = 1
print('{} || {}'.format(n1, n2), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(' || {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont = cont + 1
'''

########## DESAFIO 64 ##########
'''
soma = 0
num = 0
qtd = 0
while num != 999:
    num = int(input('digite um numero, se voce digitar 999, o programa para: '))
    soma = num + soma
    qtd += 1

print('foram digitados {} numeros'.format(qtd - 1))
print('a soma é: {}'.format(soma - 999))
'''

########## DESAFOP 65 #########
'''
op = 's'
qtd = 0
soma = 0
ma = 0
me = 999999999999999999999999999999999999999
while op == 's':
    num = int(input('digite um numero: '))
    if num > ma:
        ma = num
    if num < me:
        me = num
    soma += num
    qtd += 1
    op = str(input('ainda quer continuar? [s/n]'))
media = soma / qtd
print('o maior numero é: {}'.format(ma))
print('o menor numero é: {}'.format(me))
print('a media é: {}'.format(media))
'''
