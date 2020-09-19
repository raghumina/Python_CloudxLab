# health management system

# Lets start
def getdate():
    import datetime
    return datetime.datetime.now()


def client_data(num1,num2):
    if num1 == 1 and num2 == 1:
        f = open("file1_diet.txt","r+")
        content = f
        print(content)
    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt","r+")
        content = f
        print(content)

    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt", "r+")
        content = f
        print(content)

    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt", "r+")
        content = f
        print(content)


    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt", "r+")
        content = f
        print(content)

    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt", "r+")
        content = f
        print(content)
        
    elif num1 == 1 and num2 == 2:
        f = open("file1_exercise.txt", "r+")
        content = f
        print(content)


print(''' THIS IS A HEALTH MANAGMENT SYSTEM
YOU CAN STORE AND RETRIVE THE CLIENT DATA
THIS MANAGMENT SYSTEM STORES THE CLIENT DIET AND EXERCISE DATA ''')

print('''CLIENT CODES 
1: TOM
2: JERRY
3: GOOFEY''')
num1 = int(input("Please Enter client code, enter '1',or '2', or '3': "))
print('''Enter which data you want
1: diet
2: exercise''')
num2 = int(input("Enter 1 or 2: "))
print('''Enter what do you want to do with that data
1: Retrive 
2: Append''')
num3 = int(input("Enter 1 or 2: "))

