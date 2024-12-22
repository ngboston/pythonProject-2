#   Завдання 1
#  Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
# якщо ні — тільки першу третину. Решту списку не сортуйте,
# а розташуйте у зворотному порядку

from random import randint

def fun(lst, n):
    return sorted(lst[:n]) + lst[n:][::-1]

a = [randint(-10, 11) for _ in range(11)]
# a = list(map(int, input().split()))
m = len(a)
k = m // 3 + (m == 0)
print(a)
res = fun(a, (1 + (sum(a) / k > 0)) * k)
print(res)

