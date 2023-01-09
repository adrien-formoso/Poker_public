import random

'''
le premier chiffre des numéros de cartes permet de savoir si les info corresponde au joueur ou à l'IA
1 = joueur
0 = ia

fonctionnement des cartes possédé par les joueurs :

exemple : 
player_card = "1079"

1 0 7 9
^ ^ ^ ^
| | | |
| | | |
| | | sa derniere carte est un 10 (9+1)
| | sa deuxieme carte est un 8 (7+1)
| sa premiere carte est un 1 (0+1)
c'est le joueur (0 pour l'ia)+

pourquoi j'ai utilisé ce fonctionnement ?

- Permet de traiter facilement le chiffre 10(eviter d'avoir de confondre une carte 1 et 0 avec une carte 10)
- Permet d'avoir une seule variable par joueur pour les cartes
- Permet d'avoir une meilleur lisibilité sur les index des cartes. player_card[1] = la premiere carte du joueur

ff = forfeit

'''
############################   FONCTION   ################################
def pioche_carte(x):
  y=""
  for i in range(x):
    y = y + str(random.randint(0,9))
  return y

def affichage_info(x):
  i = 1

  if x[0] == "1":
    print("--- CARTES JOUEUR --- \n")
  else:
    print("---- CARTES DE IA --- \n")

  while i-1 < len(x)-1:
    if i != 1:
      print(int(x[i])+1," ",end="")
    else:
      print("     ",int(x[1])+1," ",end="")
    i = i +1
  
  print("\n")

  if x[0] == "1":
    print("Fond du joueur :",player_money,"€")
  else:
    print("Fond de l'IA :",ia_money,"€")

  print("-"*21)

def affichage_mise():
  print("-"*40)
  print("Mise joueur :", player_mise,"| Mise de l'IA :", ia_mise)
  print("-"*40)



def decision_player():
  print("Que désirez-vous faire ?")
  print("1 = Relancer et augmenter la mise")
  print("2 = S'arrêter et perdre la partie")
  print("3 = Mettre la même somme que l'adversaire et finir la partie")

def carte_min(x):
  y = x[1]+x[2]+x[3]
  z = 10
  for i in y:
    if int(i) < z:
      z = int(i)
  return z


###############################################################################
#########################     DECLARATION      ################################
player_money = 90
ia_money     = 90

player_mise = 10
ia_mise     = 10

player_last_mise = 0
ia_last_mise     = 0
ff =""
R = 0
decision_finale = 0
###############################################################################
########################## BOUCLE PRINCIPALE  #################################

'''
Si cette boucle s'arette la partie est terminé
'''

while player_money >0 and ia_money >0:

  # Permet de savoir que les deux joueurs sont en jeu
  player_statut = True
  ia_statut     = True

  '''
  le score des joueur
  '''
  player_score = 0
  ia_score     = 0
  player_score_test = 0
  ia_score_test     = 0


  player_card = "1"+pioche_carte(3)
  ia_card     = "0"+pioche_carte(3)

  affichage_info(player_card)
  affichage_mise()


  # Savoir qui commence
  start = random.randint(1,2)
  if start == 1:
    print("Le joueur commence\n")
  if start == 2:
    print("L'ia commence\n")

  #1 une boucle entiere = un tour de table 
  while ia_statut and player_statut: 

    if start == 1: ################## AU JOUEUR A JOUER
      decision_player()
      choise = int(input(" : ")) ##################   DECISION JOUEUR
      
      if choise == 1 : 
        choise = int(input("Choississez une valeur : "))
        player_last_mise = choise

        if choise > player_money:
          print("le montant est trop élevé")
          affichage_info(player_card)
          start = 1
        elif choise < 10:
          print("le montant est trop petit")
          affichage_info(player_card)
          start = 1
        else:
          player_mise = player_mise + choise
          player_money = player_money - choise
          affichage_info(player_card)
          start = 2


      elif choise == 2:

        player_statut = False
        ff = "PLAYERFF"
        print("\nVous avez ff :( ...")

      elif choise == 3:
        if player_mise == ia_mise:

          affichage_mise()
          player_statut = False
          print("Vous avez égalisé et cloturé")
        else :

          player_mise = player_mise + ia_last_mise
          player_money = player_money - player_mise
          player_statut = False
          affichage_mise()
          print("Vous avez égalisé et cloturé")


    if start == 2: ################## A L'IA JOUEUR A JOUER
      
      choise = random.randint(1,3) ##################   DECISION RANDOM DE L'IA
      
      
      if choise == 1:
        if ia_money < 10:
          ff = "iaoutmoney"
          ia_statut = False
        
        if ia_money < player_last_mise:
          choise = random.randint(2,3)

        if player_last_mise < 10:
          choise = random.randint(10,ia_money)
        
        else:
          choise = random.randint(player_last_mise,ia_money)
        
        ia_last_mise = choise
        print("L'ia rajoute",choise)
        ia_mise = ia_mise + choise
        ia_money = ia_money - choise 
        affichage_mise()
        start = 1

      if choise == 2:

        ia_statut = False
        ff = "IAFF"
        print("\nL'ia à ff !!!! :)")

      if choise == 3:
        if player_mise == ia_mise:

          affichage_mise()
          ia_statut = False
          print("\nL'ia a égalisé et à cloturé")
        else:

          ia_mise = ia_mise + player_last_mise
          ia_money = ia_money - ia_mise
          ia_statut = False
          affichage_mise()
          print("\nL'ia a égalisé et à cloturé")
        
  #################### SAVOIR QUI A GAGNE LA MANCHE

  affichage_info(player_card)
  affichage_info(ia_card)

  if ff == "IAFF":
    R = 1
    print("le joueur à gagné car l'ia a ff")

  elif ff == "PLAYERFF":
    R = 2
    print("L'ia à gagné car tu ff")

  ia_score_test = ia_card[1]*3
  player_score_test = player_card[1]*3
  

  if  carte_min(ia_card) + carte_min(ia_card)+1 + carte_min(ia_card)+2 == int(ia_card[1])+int(ia_card[2])+int(ia_card[3]):
    ia_score = int("4" + max(ia_card))

  elif ia_score_test == ia_card[1]+ia_card[2]+ia_card[3]:
    ia_score = int("3" + max(ia_card))
  
  elif ia_card[1] == ia_card [2] or ia_card[1] == ia_card[3] or ia_card [2] == ia_card [3]:
    ia_score = int("2" + max(ia_card))
  
  else:
    ia_score = int("1" + max(ia_card))



  if carte_min(player_card) + carte_min(player_card)+1 + carte_min(player_card)+2 == int(player_card[1])+int(player_card[2])+int(player_card[3]):
    player_score = int("4" + max(player_card))

  elif player_score_test == player_card[1]+player_card[2]+player_card[3]:
    player_score = int("3" + max(player_card))
  
  elif player_card[1] == player_card [2] or player_card[1] == player_card[3] or player_card [2] == player_card [3]:
    player_score = int("2" + max(player_card))
  
  else:
    player_score = int("1" + max(player_card))

  

  

  if R == 1:
    print("--------------- tu as GAGNE cet manche ---------------- ")
    player_money = player_money + player_mise + ia_mise
    decision_finale = 1

  elif R==2:
    print("--------------- tu as PERDUE cet manche --------------- ")
    ia_money = ia_money + ia_mise + player_mise
    decision_finale = 2

  elif player_score > ia_score:
    print("--------------- tu as GAGNE cet manche ---------------- ")
    player_money = player_money + player_mise + ia_mise
    decision_finale = 1

  elif ia_score > player_score:
    print("--------------- tu as PERDUE cet manche --------------- ")
    ia_money = ia_money + ia_mise + player_mise
    decision_finale = 2
  else:
    player_money = player_money + player_mise
    ia_money = ia_money + ia_mise


  player_mise = 10
  player_money = player_money - player_mise

  ia_mise = 10
  ia_money = ia_money - ia_mise




if decision_finale == 1:
  print(" TU AS GANNEEE LA PARTIIEE !!!!!")

else:
  print("tu as perdue la partie .......")