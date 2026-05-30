from random import randint
#sorteio
print("Jogo de adivinhação! (1-100)")
tent = 0
num = randint(1,100)
chute = 0
#loop
while chute != num:
  chute = int(input("Chute: "))
  tent = tent+1
  if chute>num:
    print("Chutou alto!")
  elif chute<num:
    print("chutou baixo!")
  else:
    print("Acertou!")
#tentativa
    print("tentativas: ", tent)
  
