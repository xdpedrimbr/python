#import math
#num = int(input('digite um numero: '))
#raiz = math.sqrt(num)
#print('a raiz de {} é {}'.format(num, raiz))
#print('a raiz de {} é, aproximadamente(para cima) {}'.format(num, math.ceil(raiz)))
#print('a raiz de {} é, aproximadamente(para baixo) {}'.format(num, math.floor(raiz)))

#import random
#num = random.randint(1, 10)
#print(num)

#import emoji
#print(emoji.emojize('ola, mundo :tired_face: ', use_aliases=True))

############# DESAFIO 16 ###############
#import math
#n = float(input('digite um numero: '))
#print('o numero sem suas casa decimais é: {}'.format(math.floor(n)))

############## DESAFIO 17 ##############
#c1 = float(input('digite o primeiro cateto: '))
#c2 = float(input('digite o segundo cateto: '))
#h = (c1**2 + c2**2)**(1/2)
#print('a hipotenusa vale: {}'.format(h))

############## DESAFIO 18 ###############
#import math
#an = float(input('digite o angulo que voce deseja: '))
#cos = math.cos(math.radians(an))
#sen = math.sin(math.radians(an))
#tan = math.tan(math.radians(an))
#print('o cosseno do angulo é {:.1f}, o seno é {:.1f} e a tangente é {:.1f}'.format(cos, sen, tan))

############## DESAFIO 19 ###############
#import random
#nome1 = str(input('digite o nome do primeiro aluno: '))
#nome2 = str(input('digite o nome do segundo aluno: '))
#nome3 = str(input('digite o nome do terceiro aluno: '))
#nome4 = str(input('digite o nome do quarto aluno: '))
#lista = [nome1, nome2, nome3, nome4]
#choice = random.choice(lista)
#print('o aluno escolhido foi: {}'.format(choice))

############## DESAFIO 20 ###############
#import random
#nome1 = str(input('digite o nome do primeiro aluno: '))
#nome2 = str(input('digite o nome do segundo aluno: '))
#nome3 = str(input('digite o nome do terceiro aluno: '))
#nome4 = str(input('digite o nome do quarto aluno: '))
#lista = [nome1, nome2, nome3, nome4]
#random.shuffle(lista)
#print('a ordem de apresentacao sera: {}'.format(lista))

############### DESAFIO 21 #################
#import pygame
#pygame.init()
#pygame.mixer.music.load('teste.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()