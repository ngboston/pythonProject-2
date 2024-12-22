#    Завдання 1
#  Напишіть функцію, яка підраховує суму елементів
# списку цілих. Список передається як параметр.

print("\n Task 1")

import random

def sumE(*num):
   return sum(num)
num = [random.randint(-100, 100) for _ in range(20)]

print(num)
print(f"sum of elements in the list: {sumE(*num)}")


#   Завдання 2
#  Напишіть функцію, яка знаходить максимум у списку
# цілих. Список передається як параметр.

print("\n Task 2")

def maxE(*num):
 num = [random.randint(-100, 100) for _ in range(20)]
 a=num
 for i in num:
      if i>0:
          a=i
 return a

print(num)
print(f"The maximum in the list: {maxE(*num)}")


#   Завдання 3
#  Напишіть функцію, яка визначає кількість парних,
# непарних, додатних, від’ємних елементів списку цілих.
# Список передається як параметр.

print("\n Task 3")

def findN(*args):
 num = [random.randint(-100, 100) for _ in range(20)]
 numEv=0
 numOdd=0
 numPos=0
 numNeg=0
 for i in args:
     if i%2==0:
        numEv+=1
     else:
         numOdd+=1
     if i>0:
          numPos+=1
     else:
         numNeg+=1
 return[numEv,numOdd,numPos,numNeg]
f=findN(*num)
print(num)
print(f" Even: {f[0]}, Odd: {f[1]}, Positive: {f[2]}, Negative: {f[3]}")


#   Завдання 4
#  Напишіть функцію, що перевертає вміст списку цілих.

print("\n Task 4")

def flipsN(num):
    return num[::-1]
num = [-80,-20,10,5,9,18,33]
print(num)
print(flipsN(num))


#   Завдання 5
# Напишіть функцію, яка шукає певне число в списку
# цілих.

print("\n Task 5")

def findN(N,f):
    if f in N:
        return True, [k for k,i in enumerate(N) if f==i]
    else:
        return False,[]
num = [-80,-20,10,5,9,18,33]
f=10
print(f"{num}\n Find number: {f}\n", findN(num,f))

#   Завдання 6
#  Напишіть функцію, яка підраховує факторіал кожного
# елемента списку цілих. Функція повертає новий список,
# що містить отримані факторіали.

print("\n Task 6")

def factorial (n):
    if n < 0:
        return ""
    fact = 1
    for number in range(1,n+1):
       fact = fact * number
    return fact
my_numbs = [1,2,3,4,5,]
result = list(map(factorial , my_numbs))
print(my_numbs)
print(f"Factorial: ", result)
