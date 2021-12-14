#random_num_list.py
#Lord Alya Vijana

#Made this at on my break at work to practice random number generation in python

from random import seed
from random import random

seed(12000)

rand_list = []

for _ in range(1000):
    rand_list.append(random())


for _ in rand_list:
    print(_)


