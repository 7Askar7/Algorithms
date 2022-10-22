import random
from math import *
birds_roi = set()
while len(birds_roi) < 100:
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    x_vec = random.randint(-50,50)
    y_vec = random.randint(-50,50)
    birds_roi.add(((x,y), (x,y),(x_vec, y_vec)))# координаты x,y и лучшая персональная позиция и вектор скорости
birds_roi = list(birds_roi)
#print(birds_roi)

#Формула для функции "Подставка для яиц"
def func(x,y):
    """a = sqrt(fabs(y+x/2+47))
    b = sqrt(fabs(x - (y + 47)))
    c = -(y+47)*sin(a)-x*sin(b)"""
    num = (sin((x**2 + y**2)**2)**2) - 0.5
    den = (1 + 0.001*(x**2 + y**2))**2
    return 0.5 + num/den

#Функция чтобы получить новый вектор куда будет двигаться точка
def get_new_vector(ind):
    new_vector_speed = ()
    speed = 0.1
    new_speed_component = 0
    for i in range(2):
        new_speed_component = birds_roi[ind][2][i] + speed * random.uniform(0,1) * (birds_roi[ind][1][i] - birds_roi[ind][0][i]) + speed * random.uniform(0,1) * (global_best[i] - birds_roi[ind][0][i])
        new_speed_component = round(new_speed_component)
        new_vector_speed+=(new_speed_component,)
    birds_roi[ind] = list(birds_roi[ind])
    birds_roi[ind][2] = new_vector_speed
    birds_roi[ind] = tuple(birds_roi[ind])

# Переход на следующую позицию
def NextPos(ind):
    birds_roi[ind] = list(birds_roi[ind])
    birds_roi[ind][0] = tuple(map(sum,zip(birds_roi[ind][0], birds_roi[ind][2])))
    birds_roi[ind] = tuple(birds_roi[ind])

global_best = list(birds_roi)[0][0]

# Поиск лучших
for i in range(0, 100):
    for k in range(len(birds_roi)):
        old_val_best = func(*(birds_roi[k][1]))
        new_val = func(*(birds_roi[k][0]))
        if new_val < old_val_best:
            old_val_best = new_val
            birds_roi[k] = list(birds_roi[k])
            birds_roi[k][1] = birds_roi[k][0]
            if old_val_best < func(*global_best):
                global_best = birds_roi[k][1]
    for j in range(len(birds_roi)):
        get_new_vector(j)
        NextPos(j)


print(global_best)
print(func(*list(global_best)))
print(birds_roi,end="\n")
