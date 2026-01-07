print("Welcome to the Calculator!")

def calculate(first_num,second_num,task):
    if task=="+":
        return first_num + second_num
    elif task=="-":
        return first_num - second_num
    elif task=="*":
        return first_num * second_num
    elif task=="/":
        return first_num / second_num   
    

fgo="y"
while fgo=="y":
    first_num = int(input("What is the first number?\n"))
    sgo = "y"
    while sgo == "y":
        print("+\n-\n*\n/\n")
        task = input("Pick a task\n")
        second_num = int(input("What is the second number?\n"))
        result = calculate(first_num,second_num,task)

        print(str(first_num)+" "+str(task)+" "+str(second_num)+" = "+str(result))
        sgo = input(f"Type Y to continue calculating with {result} or type n to start a new calculation?\n").lower()
        if sgo =="y":
            first_num=result       
