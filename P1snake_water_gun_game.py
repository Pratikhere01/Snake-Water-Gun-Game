import random

def gameWin(comp,you):
    if comp==you:
        return None

        
       #Conditions
    elif comp =='S':
        if you == 'G':
            return True
    elif you == 'W':
            return False

    elif comp == 'G':
        if you == 'W':
            return True
    elif you == 'S':
            return False

    elif comp =='W':
        if you == 'S':
            return True
    elif you == 'G':
        return False
print("Comp turn : Snake(S) Water(W) or Gun(G) ? ")
randNo = random.randint(1, 3)
if randNo== 1 :
    comp = "S"
elif randNo == 2:
        comp = "W"
elif randNo == 3:
    comp = "G"

you = input("Your turn : Snake(S) Water(W) Gun(G) ? ")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

#Possible Results
if a== None:
    print("The game is tie")
elif a:
        print("You win")
else:
        print("You loose")

        #My first Project on py (Snake ,Water, Gun game)



    
        


        

            