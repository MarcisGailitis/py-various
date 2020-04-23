#test file for concurency, threadings, multiple processes, etc

import time
from datetime import datetime
from concurrent import futures

n=5

def my_sleep():
    sec=2
    time.sleep(sec)
    tm=datetime.now().time()
    print(f'waited {sec} seconds. Timestamp: {tm.hour}:{tm.minute}:{tm.second}')

#regular process
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


regular(n)
threadpool(n)
#processpool(n)
