import random
p = input (f"Qual será o nome do seu personagem?\n")
person = p
vida = 10 #vida da gente 
life = 10 #vida do inimigo
inimigos = ["a", 'b','c'] #lista de inimigos
chance = ["consegue", ' não consegue']
inimigo = (random.choice(inimigos)), 


(("O inimigo encontrado foi um ", inimigo))
e = input("escolha o que você vai fazer\n Atacar (A)\n Fugir (F)\n=")


if e == "a":
    w = input ("Escolha o objeto que você vai atacar\n Arma\n Espada ")
    if w == 'Arma':
        inim = (life - 8)
        print ("a vida dele é", inim)

    elif w == 'espada':
        inim = (life - 5)
        print("a vida dele é",inim)

    else:
        print("Deixa de ser burro")

        
elif e == 'f':
    p = (random.choice(chance))
    if p == 'consegue':
        print ('Parabens, fugiu!')
    else:
        vida = (vida - 0)
        print('End game')