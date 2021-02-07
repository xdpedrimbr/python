'''
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita: ##else + if = elif
    carro.siga()
    carro.direita()
senao:
    carro.seiga()
carro.pare()
'''

'''
nome = str(input('qual é seu nome? ')).strip()
if nome == 'pedro':
    print('que nome bonito')
elif nome == 'dalton' or nome == 'maria' or nome == 'ju':
    print('seu nome é comum')
elif nome in 'ana claudia jessica juliana':
    print('nome feminino')
else:
    print('seu nome é feio')

print('tenha um bom dia, {}'.format(nome))
'''

############ DESAFIO 36 ###########
'''
vc = float(input('digite o valor da casa: '))
sc = float(input('qual o seu salario: '))
tp = int(input('em quantos meses vc vai pagar? '))

pm = vc / tp
if pm > sc*0.3:
    print('o emprestimo foi negado!')
else:
    print('o emprestimo foi feito com sucesso!')
'''

############ DESAFIO 37 #############
n = int(input('digite o numero para coversao: '))
o = int(input('digie a opcao que deseja : \n1 para binario \n2 para octal \n3 para hexa\n'))
print('escolha: ')
if o == 1:
    print('o {} convertido para binario é: {}'.format(n, bin(n)))
elif o == 2:
    print('o {} convertido para octal é: {}'.format(n, oct(n)))
elif o == 3:
    print('o {} convertido para hexa é: {}'.format(n, hex(n)))
else:
    print('opcao invalida')


############ DESAFIO 38 #############
'''
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

if n1 > n2:
    print('o primeiro é o maior!')
elif n2 > n1:
    print('o segundo é o maior!')
else:
    print('nao existe maior, os dois sao iguais!')
'''

########## DESAFIO 39 ##############
'''
id = int(input('digite sua idade: '))

if id < 18:
    res = 18 - id
    print('ainda falta {} ano(s) para voce se alistar'.format(res))
elif id == 18:
    print('ja é o momento de se alistar')
else:
    res = id - 18
    print('ja passou {} ano(s) do seu periodo do alistamento'.format(res))
'''

########## DESAFIO 40 ############
'''
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunfa nota: '))

m = (n1+n2)/2

if m < 5.0:
    print('reprovado')
elif m >= 5.0 and m <= 6.9:
    print('voce vai para a recuperacao')
else:
    print('voce esta aprovado')
'''

############ DESAFIO 41 ############
'''
id = int(input('digite sua idade: '))

if id <= 9:
    print('categoria: MIRIM')
elif id >= 10 and id <= 14:
    print('categoria: INFANTIL')
elif id >=15 and id <=19:
    print('categoria: SENIOR')
else:
    print('categoria: MASTER')
'''

########## DESAFIO 42 #############
'''
c1 = int(input('digite o primeiro cateto: '))
c2 = int(input('digite o segundo cateto: '))
h = int(input('digite a hipotenusa: '))

if c1 == c2 and c2 == h and c1 == h:
    print('é um triangulo equilatero')
elif c1 == c2 or h == c1 or h == c2:
    print('é um triangulo isosceles')
else:
    print('é escaleno')
'''

########### DESAFIO 43 #############
'''
p = float(input('digite seu peso: '))
h = float(input('digite sua altura: '))

imc = p/(h*h)
print('seu imc é {} e voce se encaixa na seguinte categoria: '.format(imc))

if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obeso')
else:
    print('obesidade morbida')
'''

########## DESAFIO 44 ###############
'''
p = float(input('digite o preco do produto: '))
o = str(input('escolha a opaco->a (a vista) / b (cartao a vista) / c (duas vezes no cartao) / d (parcelado em 3): '))

if o == 'a':
    np = p*0.9
    print('voce escolheu a opcao A e pagara {}R$'.format(np))
elif o == 'b':
    np = p*0.95
    print('voce escolheu a opcao B e pagara {}R$'.format(np))
elif o == 'c':
    np = p/2
    print('voce escolheu a opcao C e pagara duas parcelas de {}R$'.format(np))
elif o == 'd':
    np = p/3
    npj = np*1.20
    print('voce escolheu a opcao D e pagara 3 parcelas de {}R$'.format(npj))
'''

########## DESAFIO 45 #############
'''
from random import randint
objetos = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)
print('aperte 0 para pedra \naperte 1 para papel \naperte 2 para tesoura')
eu = int(input('qual é sua jogada? '))
print('a maquina jogou {}'.format(objetos[maquina]))
print('eu joguei {}'.format(objetos[eu]))

if maquina == eu:
    print('foi um empate')
elif maquina == 0:
    if eu == 1:
        print('parabens, voce ganhou')
    elif eu == 2:
        print('voce perdeu')
elif maquina == 1:
    if eu == 0:
        print('voce perdeu')
    elif eu == 2:
        print('parabens, voce gnahou')
elif maquina == 2:
    if eu == 0:
        print('parabens, voce ganhou')
    elif eu == 1:
        print('voce perdeu')
'''