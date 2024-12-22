#   Завдання 3
#  Маємо список цілих. Відсортуйте першу половину
# списку за спаданням, другу половину — за зростанням.

from random import randint

data = [randint(1, 100) for _ in range(10)]
print(data)
data = sorted(data[:5]) + sorted(data[5:], reverse=True)
print(data)