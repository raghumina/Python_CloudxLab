# health management system

# Lets start
def getdate():
    import datetime
    return datetime.datetime.now()


def client(num):
    if num == 1:
        f1 = open("File1_exercise.txt", "r+")
    elif num == 2:
        f2 = open("file2.txt_exercise", "r+")
    elif num == 3:
        f3 = open("file3.txt_exercise", "r+")
    else:
        print("choose form above options ")


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

