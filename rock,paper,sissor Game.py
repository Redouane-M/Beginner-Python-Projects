import random
score=0
options=("rock","paper","sissor")
computer=random.choice(options)
guess=input("Choose a rock,sissor,paper and (q) to quit: ").lower()

if guess==computer:
        print("It's a tie")
        quit()
if guess.lower()=="q":
        quit()
        
elif guess.lower()=="sissor" and computer=="paper" :
        print("You won!")
        score+=10

        print(f"you won {score} points ")
        print(f"computer choice:{computer}")

elif guess.lower()=="paper" and computer=="rock" :
        print("You won!")
        score+=10

        print(f"you won {score} points ")
        print(f"computer choice:{computer}")
        
elif guess.lower()=="rock" and computer=="sissor" :
        print("You won!")
        score+=10

        print(f"you won {score} points ")
        print(f"computer choice:{computer}")
else:
        print(computer)
        print("You lost!")
        print("Good by")
        


