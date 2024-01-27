import random
import time
choice=["python","laravel","react","redux","php","java script","mango db","my sql"]
attempt=5
start_time=time.time()

while attempt>0:
    x_time=input(f"This challenge has a deadline: write q to start: ")
    if x_time.lower()=="q":
        print("start")
    else:
        quit()

    print(f"Welcome to the Guessing the word: ")
    guess=input(f"Guess the word: ")
    
    computer=random.choice(choice) 
    if guess.lower()==computer:
        print("Congrats you guessed the right word")
        print(f"this is the word:{computer}")
        quit()

    else:
        print("Incorrect guess")
        attempt-=1

    if time.time()-start_time>20:
        print(f"Times up")
        quit()

print(f"{computer} this is the word")
        
        


