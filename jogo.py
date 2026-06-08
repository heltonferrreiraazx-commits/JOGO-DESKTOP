import random
import time
import math
person = input (f"Qual será o nome do seu personagem?\n")

vida = 10 #vida da gente 
life = 10 #vida do inimigo
inimigos = ["dragão", 'samambaia','hittler'] #lista de inimigos
chance = ["consegue", ' não consegue']


inimigo = random.choice(inimigos)
print (f'Caracteísticas ->  nome: {person} vida: {vida} ')
time.sleep (1)
print('3...')
time.sleep (1)
print('2...')
time.sleep (1)
print('1...')
time.sleep(1)
print((f"Fala tu!\n {person}\nO inimigo encontrado foi um {inimigo}"))

while vida > 0 and life > 0:
  e1 = input(f"Escolha o que você vai fazer contra o {inimigo}\n Atacar (A)\n Fugir (F)\n=")

#opção de atacar
  if e1 == "a":
    w = input ("Escolha o objeto que você vai  atacar\n (1) Arma\n (2) Espada\n= ")
    if w == '1':
        dano = random.randint(3,6)
        life -= dano
        print (f" você causou {dano} de dano")
        
    elif w == '2':
        dano = random.randint(1,4)
        life -= dano
        print (f"você causou {dano} de dano")
    else:
        print("Deixa de ser burro")

    if inimigo == 'dragâo':
        vida -= random.randint(2,5)
    elif inimigo == 'samambaia':
        vida-= random.randint (2,3)
    elif inimigo == 'hittler':
        vida-= random.randint(1,4)

    print (f'você está com {vida}hp')

     
#opção fugir 
  elif e1 == 'f':   
    p = (random.choice(chance))
    if p == 'consegue':
        print ('Parabens, fugiu!')
    


    else:
        vida = vida - random.randint(1,9)
        if vida <= 0:
           print (' Cabou a farra ')
           break
        else:
           print (f'voce foi covarde e por isso recebeu esta com {vida}hp')
  else:
     print ('num pode')
  if vida <= 0:
     print ('você foi morto... \nGame over')
     break
  elif life <= 0:
     print(f'congratulations, você derrotou o {inimigo} ')
           
time.sleep(3)
        
       
