from random import randint
#sorteio
print("Jogo de adivinhação! (1-100)")
tent = 0
num = randint(1,100)
chute = 0
#loop
while chute != num:
  chute = int(input("Try: "))
  tent = tent+1
  if chute>num:
    print("Too high!")
  elif chute<num:
    print("Too low!")
  else:
    print("You win!")
#tentativa
    print("You try: ", tent)
  
