#!/usr/bin/python3
# test file for concurency, threadings, multiple processes, etc

import time
from datetime import datetime
from concurrent import futures


# define "time consuming" process
def my_sleep():
    how_long = 2
    time.sleep(how_long)
    time_now = datetime.now().time()
    print(f'waited {how_long} seconds.'
          f'Timestamp: {time_now.hour}:{time_now.minute}:{time_now.second}')


# define decorector, to centralize logging
def timer(func):
    def wrapper(n):
        start_time = datetime.now()
        func(n)
        print(f'Done in {datetime.now()-start_time}')
        print()  # add extra blank line
    return wrapper


# regular flow
@timer
def regular(n):
    print(f'Using serial flow:')
    for n in range(1, n+1):
        my_sleep()


# parallel threads
@timer
def threadpool(n):
    excecutor = futures.ThreadPoolExecutor()
    for n in range(1, n+1):
        excecutor.submit(my_sleep)
    print(f'Using paraller threading:')
    excecutor.shutdown()


# parallel processes
@timer
def processpool(n):
    excecutor = futures.ProcessPoolExecutor()
    for n in range(1, n+1):
        excecutor.submit(my_sleep)
    print(f'Using paraller processes:')
    excecutor.shutdown()


def main():
    how_many_times = 10
    regular(how_many_times)
    threadpool(how_many_times)
    processpool(how_many_times)


if __name__ == '__main__':
    main()
