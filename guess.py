import random 

secret = random.randint(1,100)


guess = int(input("guess number (1-100):"))

if guess == secret:
    print("You win")
else:
    print("You lose! Number was", secret)