#   Завдання 1
#  Користувач вводить з клавіатури два числа. Розрахуйте
# окремо суму парних, непарних та чисел, кратних 9 у вказаному
# діапазоні, а також середнє арифметичне кожної групи.

num1 = int(input(' Enter the first number: '))
num2 = int(input(' Enter the second number: '))
sum1 = 0
count1 = 0
sum2= 0
count2 = 0
sum9 = 0
count9 = 0
for i in range(num1, num2+1):
    if i%2==0:
        sum1=sum1+i
        count1=count1+1
        avg1=sum1/count1
    if i%2!=0:
        sum2=sum2+i
        count2=count2+1
        avg2=sum2/count2
    if i%9==0:
        sum9=sum9+i
        count9=count9+1
        avg9=sum9/count9
print(' Sum of even numbers: ', sum1)
print(' Arithmetic mean for even numbers: ', avg1)
print(' Sum of odd numbers: ', sum2)
print(' Arithmetic mean for even numbers: ', avg2)
print(' The sum of multiples of nine is: ', sum9)
print(' The arithmetic mean for numbers multiples of nine: ', avg9)
