# test file for concurency, threadings, multiple processes, etc

import time
from datetime import datetime
from concurrent import futures


def my_sleep():
    how_long = 2
    time.sleep(how_long)
    time_now = datetime.now().time()
    print(f'waited {how_long} seconds.'
          f'Timestamp: {time_now.hour}:{time_now.minute}:{time_now.second}')


# regular flow
def regular(n):
    start_time = datetime.now()
    for n in range(1, n+1):
        my_sleep()
    print(f'Done in {datetime.now()-start_time}')


def threadpool(n):
    start_time = datetime.now()
    excecutor = futures.ThreadPoolExecutor()
    for n in range(1, n+1):
        excecutor.submit(my_sleep)
    print(f'\nUsing threading method:')
    excecutor.shutdown()
    print(f'Done in {datetime.now()-start_time}')


def processpool(n):
    start_time = datetime.now()
    excecutor = futures.ProcessPoolExecutor()
    for n in range(1, n+1):
        excecutor.submit(my_sleep)
    print(f'\nUsing process method:')
    excecutor.shutdown()
    print(f'Done in {datetime.now()-start_time}')


def main():
    how_many_times = 10
    regular(how_many_times)
    threadpool(how_many_times)
    processpool(how_many_times)


if __name__ == '__main__':
    main()
