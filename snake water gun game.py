import random

def game(comp, you):
    if comp==you :
        return None
    elif comp == 's' :
        if you == 'w' :
            return False
        elif you == 'g' :
            return True
    elif comp == 'w' :
        if you == 'g' :
            return False
        elif you == 's' :
            return True
    elif comp == 'g' :
        if you == 's' :
            return False
        elif you == 'w' :
            return True


print("computer turn : snake(s) water(w) gun(g) ?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("your turn : snake(s) water(w) gun(g) ?")

print(f"Computer chose {comp}")
print(f"You chose {you}")

if game(comp, you)== None :
    print("The game is tie !!")
elif game(comp, you) :
    print("You won !!!")
else :
    print("You lose")

