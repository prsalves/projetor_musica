#criar um projetor de música que faça uma musica estilo spotify
import time
from colorama import Fore, Style
import pygame
pygame.mixer.init()
musica = pygame.mixer.Sound('poesia.mp3')
musica.play()

letra = [ 
    {'musica': '', 'tempo' : 0},
    {'musica' : '...', 'tempo': 19},
    {'musica': 'Uhm, ei, ei, uhm', 'tempo': 4 },
    {'musica': 'Delacruz, ei, ei, ei', 'tempo': 5},
    {'musica': 'Brainstorming studio (prr-prr-pá)', 'tempo': 4.5},

    {'musica': 'Gavião fui feito rei, brilhava como ninguém', 'tempo': 5},
    {'musica': 'Ela sabe tudo o que eu não sei', 'tempo': 2.5},
    {'musica': 'Mas ansiava por alguém', 'tempo': 2.5},
    {'musica': 'Logo me apresentei, inocentemente ou não', 'tempo': 4.8},
    {'musica': 'Por ela eu me apaixonei', 'tempo': 2.7},
    {'musica': 'Fiel feito um gavião', 'tempo': 2.2},

    {'musica': 'Por sete mares eu voei (larara)', 'tempo': 2.5},
    {'musica': 'Mais de sete amores amei (larara)', 'tempo': 2.2},
    {'musica': 'Mais de sete vidas gastei (larara)', 'tempo': 2.5},
    {'musica': 'Aos vinte e um, te encontrei (larara)', 'tempo': 2.7},

    {'musica': 'Seja bem-vinda (larara)', 'tempo': 2},
    {'musica': 'E jamais se viu coisa tão linda (larara)', 'tempo': 2.5},
    {'musica': 'E anda comigo por que ainda (larara)', 'tempo': 3.7},
    {'musica': 'Há muito tempo pra viver (larara)', 'tempo': 2.2},

    {'musica': 'E nossas vidas baseadas em causas perdida\'', 'tempo': 4.7},
    {'musica': 'Procurando saída, ah', 'tempo': 2.5},
    {'musica': 'Ou procurando esquecer', 'tempo': 2.8},

    {'musica': 'E cada vez que eu olho nos teus olhos', 'tempo': 3},
    {'musica': 'Te espelho com desejo, eu te beijo', 'tempo': 4},
    {'musica': 'E me vejo decretando o fim', 'tempo': 3},

    {'musica': 'Tão simples como o fogo, eu tão novo não sabia', 'tempo': 4.8},
    {'musica': 'Só queria', 'tempo': 1.4},
    {'musica': 'E de novo, era um novo início pra mim', 'tempo': 5},

    {'musica': 'Viverá e verá, meu filho dará', 'tempo': 4.6},
    {'musica': 'Sorrirá, cantará, dançará sem parar, sem parar', 'tempo': 5.8},
    {'musica': 'Viverá e verá, meu filho dará', 'tempo': 4.6},
    {'musica': 'Sorrirá, cantará, dançará sem parar, sem parar', 'tempo': 5.4},

    {'musica': 'E o céu será tua casa, voará com tuas asas', 'tempo': 4.7},
    {'musica': 'Não se abalará por pouco, amaremos feito loucos', 'tempo': 5},
    {'musica': 'Será livre como nunca e sorrirá como sempre', 'tempo': 5},
    {'musica': 'Reinaremos por direito e que assim seja feito', 'tempo': 7                                   },
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
    {'musica': '', 'tempo' : 0},
]
x = 0
while True:
    print(Fore.LIGHTBLACK_EX + letra[x]['musica'] + Style.RESET_ALL)
    print(Fore.GREEN + letra[x+1]['musica'])
    print(Fore.LIGHTBLACK_EX + letra[x+2]['musica'])
    print(Fore.LIGHTBLACK_EX + letra[x+3]['musica'])
    print(Fore.LIGHTBLACK_EX + letra[x+4]['musica'])
    time.sleep(letra[x+1]['tempo'])
    for _ in range(80):
        print()
    x+=1