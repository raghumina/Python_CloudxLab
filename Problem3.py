# health management system
'''
# Lets start
def getdate():
    import datetime
    return datetime.datetime.now()


def client_data_append(num1,num2,num3):
    if num1 == 1 and num2 == 1 and num3 == 2:
        f1 = open("file1_diet.txt","r+")
        content1 = f1.write("")
        print(content1)
    elif num1 == 1 and num2 == 2 and num3 == 2:
        f2 = open("file1_exercise.txt","r+")
        content2 = f2.write("")
        print(content2)

    elif num1 == 2 and num2 == 1 and num3 == 2:
        f3= open("file2_diet.txt", "r+")
        content3 = f3.write("")
        print(content3)

    elif num1 == 2 and num2 == 2 and num3 == 2:
        f4 = open("file2_exercise.txt", "r+")
        content4 = f4.write("")
        print(content4)


    elif num1 == 3 and num2 == 1 and num3 == 2:
        f5 = open("file3_diet.txt", "r+")
        content5 = f5.write("")
        print(content5)

    elif num1 == 3 and num2 == 2 and num3 == 2:
        f6 = open("file3_exercise.txt", "r+")
        content6 = f6.write("")
        print(content6)



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



print(client_data_append(num1,num2,num3))
print(retriveData(num1,num2,num3))

KrishnaLive:
1
year
ago

'''

def getdate():
    import datetime
    return datetime.datetime.now()


def write_dirt(acess_client):
    if acess_client in list_of_clients:
        # print(list_of_clients[acess_client])
        name = acess_client
        extension = '.txt'
        f = open(name + extension, 'a')
        diet_list = input('enter today diet food : ')
        print(name + 's diet table')
        heading = 'Diet List and Time '
        f.write(diet_list)
        date = str(getdate())
        f.write(' = ')
        f.write(date)

        print(getdate())
        f.write('\n')
        f.close()
    else:
        print('you have write incorrect name .. pleaese check')


def write_exercise(acess_client):
    if acess_client in list_of_clients:
        # print(list_of_clients[acess_client])
        name = acess_client
        extension = '.txt'
        f = open(name + extension, 'a')
        exercise_list = input('enter today exercise name : ')
        print(name + 's Exercise table')

        f.write(exercise_list)
        date = str(getdate())
        f.write(' = ')
        f.write(date)

        print(getdate())
        f.write('\n')
        f.close()
    else:
        print('you have write incorrect name .. pleaese check')


def read_files_of_clients(acess_client):
    file_name = acess_client
    extension = '.txt'
    f = open(file_name + extension, 'rb')
    print(f.readlines())
    f.close()


list_of_clients = ['harry', 'rohan', 'hamad']
acess_client = input('enter names to select client and update databese : ')
do_what = input('what you want to do with client ?  1 for diet 2 for exercise 3 for readfiles')
if do_what == '1':
    write_dirt(acess_client)
if do_what == '2':
    write_exercise(acess_client)
if do_what == '3':
    read_files_of_clients(acess_client)