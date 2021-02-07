#frase = 'Curso em Video Python'

##fatiamento##
#print(frase[9:21])
#print(frase[9:21:2])##do 9 ao 21 pulando de dois em dois
#print(frase[:5])##comecao do caracter 0
#print(frase[15:])##comeca do 15 e vai ate o final
#print(frase[9::3])##comeca no 9 pulando de 3 em 3 ate o final (igual o segundo exemplo)

##analise##
#len(frase)
#print(len(frase))
#print(frase.count('o'))##conta quantas vezes aparece a letra o minuscula
#print(frase.count('o', 0, 13))##conta do 0 ao 13
#print(frase.find('deo'))##mostra onde comecao o deo
#print(frase.find('android'))##vai retornar -1, pois nao existe na string
#print('Curso' in frase)##pesquisa a palavra dentro da string

##transformacao##
#print(frase.replace('Python', 'android'))
#print(frase.upper())##coloca tudo em maiusculo
#print(frase.lower())##coloca tudo em minusculo
#print(frase.capitalize())##coloca em minusculo e a primeira letra coloca em maiusculo
#print(frase.title())##é o capitalize em todas as palavras

#fra2 = '   Aprenda Python  '
#print(fra2)
#print(fra2.strip())##tira espacoes excedentes
#print(fra2.rstrip())##remove so os ultimos espacos
#print(fra2.lstrip())##remove os espacos da esquerda

##divisao
#print(frase.split())##divisao considerando os espacos (outras strings)

'''
############# DESAFIO 22 ###############
nome = str(input('digite seu nome (apenas os dois primeiros): ')).strip()
print(nome.upper())
print(nome.lower())
corte = nome.split()
tam1 = len(corte[0])
print('o tamanho do primeiro nome é: {}'.format(tam1))
tamtot = len(nome) - nome.count(' ')
print('o tamanho total é: {}'.format(tamtot))
'''

'''
############ DESAFIO 23 ################
num = int(input('informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
'''

'''
############# DESAFIO 24 ###############
cidade = str(input('digite o nome da cidade que voce nasceu: ')).strip()
print(cidade[:5].lower() == 'santo')
'''

'''
############### DESAFIO 25 ##############
nome = str(input('digite o se nome: ')).strip()
print('seu nome tem silva? {}'.format('silva' in nome.lower()))
'''

'''
############## DESAFIO 26 #############
frase = str(input('digite uma frase: ')).strip().upper()
print('a frase tem {} letra(s) A'.format(frase.count('A')))
print('a primeira letra A apareceu na posicao: {}'.format(frase.find('A')))
print('a ultima aparicao de A é em: {}'.format(frase.rfind('A')))
'''

############# DESAFIO 27 #############
nome = str(input('digite seu nome completo: ')).strip()
separar = nome.split()
print('o seu primeiro nome é: {}'.format(separar[0]))
print('seu ultimo nome é: {}'.format(separar[len(separar)-1]))
