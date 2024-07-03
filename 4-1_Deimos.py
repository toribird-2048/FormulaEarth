#1x2行列(複素数対応)
import random
import numpy as np
import cmath

earth = []
aim = 2 + 5j
children_count = 100
crossover_count = 1000
mutation_rate = 0.1
mutation_range = 0.001
limit = 100

def formula(a: np.array):
    return complex(a[0],a[1]).conjugate()

def distance(a: np.array):
    return abs(formula(a).real - aim.real) + abs(formula(a).imag - aim.imag)

def generate(min,max,count):
    global earth
    earth = []
    for k in range(count):
        earth.append(np.array([random.uniform(min,max),random.uniform(min,max)]))

def crossover():
    global children_count
    global earth
    global aim
    global crossover_count
    for l in range(crossover_count):
        dad = random.choice(earth)
        mam = random.choice(earth)
        for k in range(children_count):
            rate = random.uniform(0,1)
            earth.append(dad*rate + mam*(1-rate))

def mutation():
    global earth
    global mutation_rate
    global mutation_range
    for k in range(len(earth)):
        if random.uniform(0,1) < mutation_rate :
            earth[k] += np.array([random.uniform(-mutation_range,mutation_range),random.uniform(-mutation_range,mutation_range)])

def limitting():
    global earth
    global aim
    global limit
    earth.sort(key=lambda x: distance(x))
    if len(earth) > limit :
        earth = earth[:limit]

def process(n):
    for k in range(n):
        crossover()
        mutation()
        limitting()
        print(k,earth[0])
    
generate(-100,100,children_count)
process(200)

print(neo_earth[0])
print(formula(neo_earth[0]))