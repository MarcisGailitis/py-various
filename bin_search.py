# Binary Search program:
# generates sorted list of lenght n
# deletes random element from the list
# finds deleted element using Binary Search
# should change the setup to functions + handle edge cases
import random
from datetime import datetime

len_list = 10_000_000

start_time = datetime.now()
# initiate list of sorted elements with lenght n
list_of_nrs = [x for x in range(1, len_list+1)]
print(f"Initial len: {len(list_of_nrs)}")

# delete randon element from the list
random_nr = random.randint(0, len_list-1)
del list_of_nrs[random_nr]
print(f"Deleted element: {random_nr+1}, updated len: {len(list_of_nrs)}\n")

# initiated Binary search
counter = 0

left = 0
right = len(list_of_nrs)
while left <= right:
    counter += 1
    middle = (left+right)//2
    print(f"Run nr: {counter}, left/middle/right: {left}/ {middle} / {right}")

    # should update work with edge cases
    if len(list_of_nrs[left:right+1]) <= 3:
        final_nrs = list_of_nrs[left:right+1]
        for pos, nr in enumerate(final_nrs):
            if nr+1 == final_nrs[pos+1]:
                continue
            else:
                print(nr+1)
                break
        break

    if list_of_nrs[middle] > middle+1:
        # print('> ',list_of_nrs[middle],middle+1)
        right = middle

    if list_of_nrs[middle] == middle+1:
        # print('==',list_of_nrs[middle],middle+1)
        left = middle

print(f'time passed {datetime.now()-start_time}')
