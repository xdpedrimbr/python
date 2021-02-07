'''
for c in range(1, 10):
    print('oi')
print('fim')
for c in range(0, 10):
        print('oi')
'''

'''
for a in range(0, 6):
    print(a)
print('#########################')
for b in range(6, 0, -1): ##decresente
    print(b)
print('#########################')
for c in range(0, 10, 2): ##de dois em dois
    print(c)
'''

'''
n = int(input('digite um numero: '))
for i in range(0, n+1):
    print(i)
print('fim')
'''

'''
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
'''

'''
s = 0
for c in range(0, 10):
    n = int(input('digite um valor: '))
    s += n
print('o somatorio é: {}'.format(s))
'''

########## DESAFIO 46 ############
'''
print('os fogos irao estourar em.....')
for c in range(10, 0, -1):
    print('{} segundo(s)'.format(c))
'''

############ DESAFIO 47 ###########
'''
s = 0
for c in range(0, 500, 3):
    s += c
print('a soma dos multiplos de 3 é: {}'.format(s))
'''

########### DESAFIO 48 ##############
'''
for c in range(0, 51):
    if c%2==0:
        print(c)
'''

############## DESAFIO 49 ###########
'''
n = int(input('digite um numero para ver a tabuada: '))
print('a tabuada do numero é: ')
for c in range(1, 10):
    tab = n * c
    print(tab)
'''

########### DESAFIO 50 ###############
'''
sp = 0
for c in range(0, 6):
    n = int(input('digite um numero: '))
    if n%2==0:
      sp = sp + n
print('a soma dos numeros pares é: {}'.format(sp))
'''

########## DESAFIO 51 ##############
'''
p1 = int(input('digite o primeiro numero: '))
r = int(input('digite a razao da PA: '))
print('o 1º termo é: {}'.format(p1))
for c in range(2, 11):
    p1 = p1 + r
    print('o {}º termo é: {}'.format(c, p1))
'''

########### DESAFIO 52 ##############
'''
n = int(input('digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('ele é primo')
else:
    print('ele nao é primo')
'''

########### DESAFIO 53 #############
'''
frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso += juntar[letra]
print(juntar, inverso)
if juntar == inverso:
    print('é palindromo')
else:
    print('nao é palindomo')
'''

########### DESAFIO 54 #############
'''
print('considere que estamos no ano de 2018')
for c in range(1, 8):
    a = int(input('digite o seu ano de nascimento: '))
    if 2018 - a >= 18:
        print('a pessoa de numero {} é maior de idade'.format(c))
    else:
        print('a pessoa de numero {} NAO é maio de idade'.format(c))
'''
########## DESAFIO 55 ############
'''
ma = 0
me = 0
for p in range(1, 6):
    peso = float(input('digite o peso da {}º pessoa: '.format(p)))
    if p == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print('o maio peso é {} e o menor {}'.format(ma, me))
'''

########## DESAFIO 56 ############
si = 0
mi = 0
maidh = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('{}ª pessoa:'.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo(M ou F): ')).strip()
    si = si + idade
    if c == 1 and sexo in 'Mm':
        maidh = idade
        nomevelho = nome
    if sexo in  'Mm' and idade > maidh:
        maidh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mi = si/4
print('a media da idade é: {}'.format(mi))
print('o homem mais velho tem {} anos e é o {}'. format(maidh, nomevelho))
print('a qtd de mulheres com menos de 20 anos é {}'.format(totmulher20))