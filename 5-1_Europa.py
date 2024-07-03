#1xn行列,rng対応
import random
import numpy as np
import cmath

earth = []
length = 4
aim = 0
children_count = 100
crossover_count = 1000
mutation_rate = 0.1
mutation_range = 1
limit = 100

rng = np.random.default_rng()

def formula(a: np.array):
    x = (a[0] / a[1]) + cmath.sqrt(a[2] / a[3])
    return x*2 + 2*x + 1

def distance(a: np.array):
    return np.sum(abs(formula(a) - aim))

def generate(min,max,count):
    global earth
    earth = []
    for k in range(count):
        earth.append(np.array([rng.integers(min,max) for k in range(length)]))

def crossover():
    global children_count
    global earth
    global aim
    global crossover_count
    for l in range(crossover_count):
        dad = random.choice(earth)
        mam = random.choice(earth)
        for k in range(children_count):
            rate = rng.integers(0,1)
            earth.append(dad*rate + mam*(1-rate))

def mutation():
    global earth
    global mutation_rate
    global mutation_range
    for k in range(len(earth)):
        if rng.integers(0,1) < mutation_rate :
            mutation_place = random.randint(0,length)
            earth[k] += np.array([rng.integers(-mutation_range,mutation_range) if k == mutation_place else 0 for k in range(length)])

def limiting():
    global earth
    global aim
    global limit
    earth.sort(key=lambda x: distance(x))
    if len(earth) > limit :
        earth = earth[:limit]

def process(n):
    for k in range(n):
        mutation()
        crossover()
        limiting()
        print(k,earth[0])


generate(-10,10,children_count)
process(200)
print(earth[0])
print(formula(earth[0]))