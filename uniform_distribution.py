import random
from random import randint
w = [0, 1, 2, 3, 4, 5]
i = [1, 2, 3, 4, 5, 6]

def uniform_pick(i):
    dice = randint(0, len(i)-1)
    return i[dice]

def random_pick(w, i):
    l = list()
    for j in range(0, len(w)):
        times = w[j]
        for k in range(0, times):
            l.append(i[j])
    random.shuffle(l)
    index = randint(0,len(l)-1)
    return l[index]
for j in range(0, 100):
    #print(uniform_pick(i))
    print(random_pick(w,i))
