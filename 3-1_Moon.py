#1x1行列(numpy.random)
import random
import math
import numpy as np

earth = []
aim = 4
children_count = 100
crossover_count = 500
mutation_rate = 0.01
mutation_range = 0.1
limit = 1000



def formula(x):
    return x**

def distance(x):
    return abs((formula(x) - aim))    

def generate(min,max,count):
    global earth
    earth = []
    for k in range(count):
        earth.append(rng.uniform(min,max))

def crossover():
    global children_count
    global earth
    global aim
    global crossover_count
    for l in range(crossover_count):
        dad = random.choice(earth)
        mam = random.choice(earth)
        for k in range(children_count):
            rate = rng.uniform(0,1)
            earth.append(dad*rate + mam*(1-rate))

def mutation():
    global earth
    global mutation_rate
    global mutation_range
    for k in range(len(earth)):
        if rng.uniform(0,1) < mutation_rate :
            earth[k] += rng.uniform(-mutation_range,mutation_range)

def limiting():
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
        limiting()
        print(k,earth[0])

generate(-100,100,children_count)
process(100)
print(earth[0])
print(formula(earth[0]))