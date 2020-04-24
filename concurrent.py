#test file for concurency, threadings, multiple processes, etc\

import time
from datetime import datetime
from concurrent import futures


def my_sleep():
    sec = 2
    time.sleep(sec)
    time_now = datetime.now().time()
    print(f'waited {sec} seconds. Timestamp: {time_now.hour}:{time_now.minute}:{time_now.second}')


# regular process
def regular(n):
    start_time=datetime.now()
    for n in range(1,n+1):
        my_sleep()
    print(f'Done in {datetime.now()-start_time}')

    
def threadpool(n):
    start_time = datetime.now()
    excecutor = futures.ThreadPoolExecutor()
    for n in range(1,n+1):
        excecutor.submit(my_sleep)
    print(f'\nUsing threading method:')
    excecutor.shutdown()
    print(f'Done in {datetime.now()-start_time}')


def processpool(n):
    start_time=datetime.now()
    excecutor = futures.ProcessPoolExecutor()
    for n in range(1,n+1):
        excecutor.submit(my_sleep)
    print(f'\nUsing process method:')
    excecutor.shutdown()
    print(f'Done in {datetime.now()-start_time}')

    
def main():
    n=10
    regular(n)
    threadpool(n)
    processpool(n)

    
if __name__ == '__main__':
    main()
