import asyncio
import time
from random import randint

start_time = time.time()
arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = 0


async def sum_num(num_list):
    global sum_
    for num in num_list:
        sum_ += num


async def main():
    tasks = []
    for i in range(10):
        start_ind = i * 100_000
        end_ind = start_ind + 100_000
        task = asyncio.create_task(sum_num(arr[start_ind:end_ind]))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print(sum_)
print(f'{time.time() - start_time:.2f}')
