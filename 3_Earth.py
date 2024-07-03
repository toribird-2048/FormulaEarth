#1x1行列
import random
import math

earth = []
aim = 12_3456_7890
children_count = 100
crossover_count = 1000
mutation_rate = 0.1
mutation_range = 500
limit = 100

def formula(x):
    return x**2

def generate(min,max,count):
    global earth
    earth = []
    for k in range(count):
        earth.append(random.uniform(min,max))

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
            earth[k] += random.uniform(-mutation_range,mutation_range)

def limiting():
    global earth
    global aim
    global limit
    earth.sort(key=lambda x: abs(formula(x)-aim))
    if len(earth) > limit :
        earth = earth[:limit]

def process(n):
    for k in range(n):
        crossover()
        mutation()
        limiting()
        print(k,earth[0])

generate(-10,10,children_count)
process(200)
print(earth[0])