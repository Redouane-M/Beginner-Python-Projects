import random
low=0
high=30
guesses=0
number=random.randint(low,high)
while True:
    guess=int(input("Guess the number now: "))
    if guess==str:
        print("You should write a nimber")
        quit()
    if guess<number:
        print(f"{guess} is too low ")
        guesses+=1

    elif guess>number:
        print(f" {guess} is too high")
        guesses+=1

    else:
        print(f" {guess} is the correct guess")
        break;

print(f"You took {guesses} guesses to guess it !!")


# score=0
# question=0
# print("This is a Quiz Game")
# guess=input("Do you wanna play? :")

# if guess.lower()=="yes":
#     print("okay let's play!")
# elif guess.lower()!="yes":
#     quit()
# else:
#     print("it's your choice")

# answer=input("What is the capital of Morocco ? : ")
# if answer.lower()=="rabat":
#     print("correct!")
#     question+=1
#     score+=10
# else:
#     print("incoreect answer!")

# answer=input("What does CPU stand for ? : ")
# if answer.lower()=="central processing unit":
#     print("correct")
#     question+=1
#     score+=10
# else:
#     print("incoreect answer!")

# answer=input("What does RAM stand for ? : ")
# if answer.lower()=="random acces memory":
#     print("Correct")
#     question+=1
#     score+=10
# else:
#     print("incoreect answer!")

# answer=input("What does PSU stand for ? : ")
# if answer.lower()=="power supply":
#     print("Correct")
#     question+=1
#     score+=10

#     print(f"You've got {question} correct")
#     print(f"Your score is : {score}  points")

# else:
#     print("incorect answer!")
    

        



