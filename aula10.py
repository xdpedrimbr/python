'''
if carro.esquerda:
    bloco True

else:
    bloco False
'''

'''
tempo = int(input('quantos anos tem seu carro: '))
    if tempo <= 3:
        print('carro novo')
    else:
        print('carro velho')
    print('===FIM===')
'''

'''
nome = str(input('qual seu nome? '))
if nome == 'pedro':
    print('que nome lindo')
else:
    print('seu nome é feio')
print('bom dia {}'.format(nome))
'''

'''
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('a media da nota é: {:.1f}'.format(m))
if m >= 60.0:
    print('aprovado')
else:
    print('reprovado')
'''

############ DESAFIO 28 ###########
'''
import random
pc = random.randint(0, 5)
print('apenas para testes: {}'.format(pc))
usu = int(input('digite um numero entre 0 e 5: '))
if pc == usu:
    print('voce acertou o numero sorteado')
else:
    print('voce digitou o numero errado')
'''

########### DESFIO 29 ###########
'''
v = float(input('digite a velocidade do carro: '))
if v > 80.0:
    d = v - 80.0
    p = d * 7.0
    print('voce ultrapassou a velocidade em {}km/h e tera que pagar {}R$'.format(d, p))
else:
    print('voce nao foi multado')
'''

########## DESAFIO 30 ###########
'''
n = int(input('digite um numero: '))
if n %2==0:
    print('o numero é par')
else:
    print('o numero é impar')
'''

########## DESAFIO 31 ##########
'''
d = float(input('digite a distancia da biagem: '))
if d > 200:
    t = d*0.45
    print('o valor sera: {}'.format(t))
else:
    t2 = d*0.5
    print('o valor sera: {}'.format(t2))
'''

######### DESAFIO 32 ##########
'''
ano = int(input('digite o ano: '))
if ano %4==0 and ano %100!=0 and ano %400==0:
    print('o ano é bissexto')
else:
    print('o ano nao é bissexto')
'''

########## DESAFIO 33 ##########
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if n1<n2 and n1<n3:
    menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('o menor é: {}'.format(menor))

if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('o maior é: {}'.format(maior))



########## DESAFIO 34 ##########
'''
s = float(input('digite seu salario: '))
if s > 1250.0:
    ns = s * 1.1
    print('o novo salario é: {}'.format(ns))
else:
    ns = s * 1.15
    print('o novo salario é: {}'.format(ns))
'''

########## DESAFIO 35 ##########
'''
c1 = int(input('digite o primeiro cateto: '))
c2 = int(input('digite o segundo cateto: '))
h = int(input('digite a hipotenusa: '))

if c1 + c2 > h:
    print('é possivel formar um triangulo')
else:
    print('nao é pssivel formar um triangulo')
'''