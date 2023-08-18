# 7. Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
#    Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#    Массив должен быть заполнен случайными целыми числами от 1 до 100.
#    При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
#    В каждом решении нужно вывести время выполнения вычислений

import threading
import time
from random import randint

start_time = time.time()
arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = 0


def sum_num(num_list):
    global sum_
    for num in num_list:
        sum_ += num


threads = []
for i in range(10):
    start_ind = i * 100_000
    end_ind = start_ind + 100_000
    thread = threading.Thread(target=sum_num, args=(arr[start_ind:end_ind],))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(sum_)
print(f'{time.time() - start_time:.2f}')
