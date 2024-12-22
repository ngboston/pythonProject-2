#   Завдання 1
#  Напишіть рекурсивну функцію знаходження степені
# числа.

print("\n Task 1")


def power(N, P):
    if P == 0:
        return 1
    if P % 2 == 0:
        result = power(N, P // 2)
        return result * result
    else:
        result = power(N, (P - 1) // 2)
        return N * result * result
if __name__ == '__main__':
    N = 5
    P = 2
print(power(N, P))

#  Завдання 2
#  Напишіть рекурсивну функцію, яка обчислює суму
# всіх чисел у діапазоні від a до b. Користувач вводить a та
# b. Покажіть приклад роботи функції.

print("\n Task 2")

def sum_range(a, b):
    if a > b:
         return 0
    return a + sum_range(a+1, b)
print(sum_range(1, 5))


#  Завдання 3
#  Напишіть рекурсивну функцію, яка виводить в рядок
# N зірочок, число N задає користувач. Покажіть приклад
# роботи функції.

print("\n Task 3")

def print_stars(n):
    if n <= 0:
        return
    print('*', end='')
    print_stars(n-1)
print_stars(5)

#  Завдання 4
#  Створіть гру «Хрестики-Нулики».

print("\n Task 4")

print("Гра хрестик нолик для двох учасників ")
board = list(range(1,10))
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куди поставити " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некотектний хід.")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Всі комірки заповенені!")
      else:
        print("Не коректний хід. Поставтте число від 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "Виграв!")
              win = True
              break
        if counter == 9:
            print("Нічя!")
            break
    draw_board(board)
main(board)

input("Натисніть Enter для виходу!")

#  Завдання 5
#  Напишіть рекурсивну функцію, яка приймає спи
# сок із 100 цілих чисел, отриманих випадковим чином, і
# знаходить позицію, з якої починається послідовність з
# 10 чисел, сума яких мінімальна.

print("\n Task 5")

import random

def find_min_sum(arr, start=0, min_sum=float('inf'), min_pos=0):
    if start > len(arr) - 10:
        return min_pos
    current_sum = sum(arr[start:start + 10])

    if current_sum < min_sum:
        min_sum = current_sum
        min_pos = start
    return find_min_sum(arr, start + 1, min_sum, min_pos)

arr = [random.randint(1, 100) for _ in range(100)]
min_pos = find_min_sum(arr)

print(f"Позиція початку послідовності з мінімальною сумою: {min_pos}")
print(f"Сума чисел у послідовності: {sum(arr[min_pos:min_pos + 10])}")

#  Завдання 6
#  Напишіть функцію, яка приймає дві дати (тобто
# функція приймає шість параметрів) та обчислює різ
# ницю в днях між цими датами. Для вирішення цього
# завдання напишіть також функцію, яка визначає, чи є
# рік високосним

print("\n Task 6")

import datetime

def days_diff(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    diff = abs((date2 - date1).days)
    return diff

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

date1 = "2022-01-01"
date2 = "2022-12-31"
print(days_diff(date1, date2))

year = 2024
print(is_leap_year(year))