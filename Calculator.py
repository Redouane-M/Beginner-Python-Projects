calcul=input("What is the operation: ")
operation={
    "add" :"+",
    "subtract":"-" ,
    "multiply" :"*" ,
    "divide" :"/" 
}

if calcul in operation:
    num1=int(input("Number 1: "))
    num2=int(input("Number 2: "))
    
    if calcul=="add" or "+" :
        result=num1+num2
        
    elif calcul=="subtract" :
        result=num1-num2
        
    elif calcul=="multiply" :
        result=num1*num2

    elif calcul=="divide" :
        result=num1/num2 

    print(f"result:{result}")
else:
    print("Invalid operation")



