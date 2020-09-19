# health management system

# Lets start
def getdate():
    import datetime
    return datetime.datetime.now()


def client_data(num1,num2):
    if num1 == 1 and num2 == 1:
        f1 = open("file1_diet.txt","r+")
        content = f1
        print(content)
    elif num1 == 1 and num2 == 2:
        f2 = open("file1_exercise.txt","r+")
        content = f2
        print(content)

    elif num1 == 2 and num2 == 1:
        f3= open("file2_diet.txt", "r+")
        content = f3
        print(content)

    elif num1 == 2 and num2 == 2:
        f4 = open("file2_exercise.txt", "r+")
        content = f4
        print(content)


    elif num1 == 3 and num2 == 1:
        f5 = open("file3_diet.txt", "r+")
        content = f5
        print(content)

    elif num1 == 3 and num2 == 2:
        f6 = open("file3_exercise.txt", "r+")
        content = f6
        print(content)



def retriveData(num1,num2,num3):
    if num1 == 1 and num2 == 1 and num3 == 1:
        f1 = open("file1_diet.txt", "r+")
        content1 = f1.readlines()
        print(content1)
    elif num1 == 1 and num2 == 2 and num3 == 1:
        f2 = open("file1_exercise.txt", "r+")
        content2 = f2.readlines()
        print(content2)
    elif num1 == 2 and num2 == 1 and num3 == 1:
        f3 = open("file2_diet.txt", "r+")
        content3 = f3.readlines()
        print(content3)

    elif num1 == 2 and num2 == 2 and num3 ==1:
        f4 = open("file2_exercise.txt", "r+")
        content4 = f4.readlines()
        print(content4)

    elif num1 == 3 and num2 == 1 and num3 == 1:
        f5 = open("file3_diet.txt", "r+")
        content5 = f5.readlines()
        print(content5)

    elif num1 == 3 and num2 == 2 and num3 == 1:
        f6 = open("file3_exercise.txt", "r+")
        content6 = f6.readlines()
        print(content6)


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

