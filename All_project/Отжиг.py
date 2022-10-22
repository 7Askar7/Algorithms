import random
import math
Razmer_rukzak = 35
       #Важность, Вес
Vashnost = [(10,15),
           (10,3),
           (8,7),
           (4,4),
           (1,1),
           (7,3),
           (6,5),
           (4,1),
           (4,2),
           (8,3),
           (1,1),
           (7,2),
           (10,9)]
Predmet= ["Бронижилет","Аптечка","Патроны","Консервы","Сигаерты","Батарейки","Фонарь","Спички",
       "Зажигалка","Носки","Мыло","Перчатки","Сапоги"]
T_start = 100
T_finish = 2
rate = 0.7

Gotov_rukzak = [Vashnost[0],Vashnost[1],Vashnost[2],Vashnost[9],Vashnost[5],Vashnost[3]]

def svobod(g_r):
    vashn= set(Vashnost)
    g_r = set(g_r)
    sv = vashn.difference(g_r)
    return list(sv)
svobod(Gotov_rukzak)

def linear(T_current):
    return rate * T_current

def fit_function(sobr_rukzak):
    sum = 0
    for vesh in sobr_rukzak:
        sum+= vesh[0]
    return sum
fit_function(Gotov_rukzak)

def fit_function_ves(sobr_rukzak):
    sum = 0
    for vesh in sobr_rukzak:
        sum+= vesh[1]
    return sum
fit_function_ves(Gotov_rukzak)

def new_solution(rukzak):
    size = len(rukzak)
    rand_list = []
    for i in range(4):
        rnd = random.randint(0, size-1)
        rand_list.append(rnd)

    for j in range(len(rand_list)):
        new_item = random.choice(svobod(rukzak))
        if (fit_function(rukzak) - rukzak[rand_list[j]][1] + new_item[1]) > Razmer_rukzak:
            j-=1
            continue

        else:
            r = rukzak[rand_list[j]]
            rukzak[rand_list[j]] = new_item
    return rukzak

print(Gotov_rukzak)
#new_solution(Gotov_rukzak)
#fit_function(new_solution(Gotov_rukzak))

def h(delE,T_current):
    x = math.exp(-delE/T_current)
    return x

def main_algo():
    current_T = T_start
    count_iter = 0
    currnet_state = Gotov_rukzak
    while current_T > T_finish:
        count_iter = count_iter+1
        new_state = new_solution(Gotov_rukzak)
        delta = fit_function(Gotov_rukzak) - fit_function(new_state)
        if delta <= 0:
            currnet_state = new_state
        else:
            prob = h(delta, current_T)
            x = random.uniform(0,1)
            if prob > x:
                current_state = new_state
        current_T = linear(current_T)
    print("Итерации = ", count_iter)
    return currnet_state

main_algo()
print("Ценность = ", fit_function(main_algo()))
print("Вес = ", fit_function_ves(main_algo()))
