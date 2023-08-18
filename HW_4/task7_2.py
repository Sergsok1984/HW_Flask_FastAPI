import multiprocessing
import time
from random import randint

start_time = time.time()
arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = multiprocessing.Value('i', 0)


def sum_num(num_list, sum_):
    for num in num_list:
        with sum_.get_lock():
            sum_.value += num


if __name__ == '__main__':
    processes = []
    for i in range(10):
        start_ind = i * 100_000
        end_ind = start_ind + 100_000
        process = multiprocessing.Process(target=sum_num, args=(arr[start_ind:end_ind], sum_))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(sum_.value)
    print(f'{time.time() - start_time:.2f}')
