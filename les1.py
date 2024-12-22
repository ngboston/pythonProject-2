def meanF(*args):
    s = 0
    k = 0
    for i in args:
        s += i
        k += 1
    res = round(s/k, 2)
    def Test():
        print("test testovoi")
    return res

def printInfo(*clients):
    for i in range(len(clients)):
        if i == 0:
            print(f"login: {clients[i]}")
        elif i == 1:
            print(f"pass: {clients[i]}")

# users = [['user1', '111'],
#          ['user2', '222'],
#          ['user3', '333']]
#
# for user in users:
#     printInfo(*user)

def userGreetings(id ,userName,login="Nan", passw="111"):
    if login == "admin":
        print("Welcome admin")
        print(passw)
    elif login == "students":
        print("Welcome students")
        print(passw)
    else:
        print("Welcome, guy")
        print(passw)

def myCalculation1(a,b,c):
    return (a+b)**c

def myCalculation2(a,b,c = 50):
    return (a+b)**c

def calculationBMI(m, h):
    return m / (h**2)

def calculeteExample1():
    baseVar = int(input("enter base var: "))
    resultVar = baseVar ** 2
    print(f"The square of {baseVar} is {resultVar}")



def checkUser():
    userLog = input("enter login: ")
    global userName
    userName = "Jane"
    if userLog == "admin":
        print(f"{userName} is admin")
    else:
        print(f"{userName} is not admin")

def howdyUser():
    global userLog
    userLog = "admin"
    print("Welcome")
    return userLog
def checkPassword(password):
    howdyUser()
    if userLog == "admin" and password == "111":
        print(f"{userLog} is admin")
    elif userLog == "student" and password == "222":
        print(f"{userLog} is student")
    else:
        print(f"{userLog} access denied")

userLog = input("enter login: ")
userPassword = input("enter password: ")

checkPassword(userPassword)

from random import randint
numbers = [randint(-100, 100) for _ in range(20)]
