import random
import sys


n = 2           #Количество частиц
coord_y = [0] * n    #Координата частицы y
coord_x = [0] * n    #Координата частицы x
speed_v = [0] * n    #Скорость частицы
a1 = 2          #Ускорение
a2 = 2          #Ускорение
pbest = [0] * n      #Лучшая позиция частицы
gbest = -100    #Наилучшая возможная позиция
vmax = 0.1      #Максимальная скорость

def fitnessFunction():           #Функция приспособленности
    for i in range(n):
        coord_y[i] = (-1 * coord_x[i] * (coord_x[i] - 2))

def init():
    for i in range(n):
        coord_x[i] = (random.uniform(-5, 5))
        speed_v[i] = (random.uniform(-5, 5))

    fitnessFunction()

    for i in range(n):
        global gbest
        pbest[i] = coord_y[i]
        if coord_y[i] > gbest:
            gbest = coord_y[i]
    print("start gbest  " + str(gbest))

def BirdSwarm(max_swarm):
    global speed_v
    global gbest
    global vmax
    for i in range(max_swarm):
        w = 0.4         #Коэффициент инерции
        for j in range(n):
            speed_v[j] = w * speed_v[j] + a1 * random.random() * (pbest[j] - coord_x[j]) + a2 * random.random() * (gbest - coord_x[j])
            if speed_v[j] > vmax:
                vmax = speed_v[j]
            coord_x[j] = coord_x[j] + speed_v[j]

        fitnessFunction()

        for j in range(n):
            pbest[j] = max(coord_y[j], pbest[j])
            if pbest[j] > gbest:
                gbest = pbest[j]
            print(str(coord_x[j]) + "   " + str(speed_v[j]))
        print("------" + str(i + 1) + "------gbest: " + str(gbest))


def main():
    init()
    BirdSwarm(100)

main()