from functions import lambd, poisson_func, service_func


time_start = 8
time_end = 19

Ai = []
Di1 = []
Di2 = []
Vi1 = []
Vi2 = []
Si = []
Wi = []
Na = 0
Nd = 0
n = 0
c1 = 0
c2 = 0
engage1 = False
engage2 = False
counter = 0
clients = []

tA = poisson_func(time_start)
t1 = float('inf')
t2 = float('inf')
while tA < time_end:
    counter += 1
    print(f'===============================Итерация {counter}=====================================')
    if tA < t1 or tA < t2:
        print('Сработал случай 1')
        print(f'tA = {tA}')
        Ai.append(round(tA, 3))
        clients.append(0)
        print(f'Пришел клиент {len(clients)}')
        t = tA
        Na += 1
        Tt = poisson_func(t)
        while not Tt:
            Tt = poisson_func(t)
        tA = Tt
        if engage1 == False and engage2 == False:
            print('Условие: engage1 == False and engage2 == False')
            y1 = service_func(lambd)
            t1 = t + y1
            n += 1
            engage1 = True
            Di1.append(round(t1, 3))
            Vi1.append(round(y1, 3))
            Si.append(round((t1 - t), 3))
            print(f't1 = {t1}')
            print(f'Клиент {clients.index(0) + 1} начал обслуживаться')
            Wi.append(0)
            clients[clients.index(0)] = 1
            print(n, c1, c2, engage1, engage2)
        elif engage1 == False and engage2 == True:
            print('Условие: engage1 == False and engage2 == True')
            y1 = service_func(lambd)
            t1 = t + y1
            n += 1
            engage1 = True
            Di1.append(round(t1, 3))
            Vi1.append(round(y1, 3))
            Si.append(round((t1 - t), 3))
            print(f't1 = {t1}')
            print(f'Клиент {clients.index(0) + 1} начал обслуживаться')
            Wi.append(0)
            clients[clients.index(0)] = 1
            print(n, c1, c2, engage1, engage2)
        elif engage1 == True and engage2 == False:
            print('Условие: engage1 == True and engage2 == False')
            y2 = service_func(lambd)
            t2 = t + y2
            n += 1
            engage2 = True
            Di2.append(round(t2, 3))
            Vi2.append(round(y2, 3))
            Si.append(round((t2 - t), 3))
            print(f't2 = {t2}')
            print(f'Клиент {clients.index(0) + 1} начал обслуживаться')
            Wi.append(0)
            clients[clients.index(0)] = 2
            print(n, c1, c2, engage1, engage2)
        elif engage1 == True and engage2 == True:
            print('Условие: engage1 == True and engage2 == True')
            n += 1
            print(f'Клиент {clients.index(0) + 1} ожидает очереди')
            Wi.append(t)
            clients[clients.index(0)] = 3
            print(n, c1, c2, engage1, engage2)
        print(n, c1, c2, engage1, engage2)

    if t1 < tA and t1 <= t2:
        print('Сработал случай 2')
        t = t1
        engage1 = False
        c1 += 1
        Nd += 1
        if n == 1 or n == 2:
            print('Условие: n == 1 or n == 2')
            n -= 1
            t1 = float('inf')
            print(f'Клиент {clients.index(1) + 1} закончил обслуживаться')
            clients[clients.index(1)] = 4
            print(n, c1, c2, engage1, engage2)
        elif n > 2:
            print('Условие: n > 2')
            n -= 1
            y1 = service_func()
            t1 = t + y1
            print(f't1 = {t1}')
            print(f'Клиент {clients.index(1) + 1} закончил обслуживаться')
            clients[clients.index(1)] = 4
            if list(map(lambda x: x > time_end, Di1)).count(True) == 0:
                engage1 = True
                Vi1.append(round(y1, 3))
                Di1.append(round(t1, 3))
                print(f'Клиент {clients.index(3) + 1} начал обслуживаться')
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 1
            print(n, c1, c2, engage1, engage2)
        print(n, c1, c2, engage1, engage2)

    if t2 < tA and t2 <= t1:
        print('Сработал случай 3')
        engage2 = False
        t = t2
        c2 += 1
        Nd += 1
        if n == 1 or n == 2:
            print('Условие: n == 2')
            n -= 1
            t2 = float('inf')
            print(f'Клиент {clients.index(2) + 1} закончил обслуживаться')
            clients[clients.index(2)] = 4
            print(n, c1, c2, engage1, engage2)
        elif n > 2:
            print('Условие: n > 2')
            n -= 1
            y2 = service_func()
            t2 = t + y2
            print(f't2 = {t2}')
            print(f'Клиент {clients.index(2) + 1} закончил обслуживаться')
            clients[clients.index(2)] = 4
            if list(map(lambda x: x > time_end, Di2)).count(True) == 0:
                engage2 = True
                Vi2.append(round(y2, 3))
                Di2.append(round(t2, 3))
                print(f'Клиент {clients.index(3) + 1} начал обслуживаться')
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 2
            print(n, c1, c2, engage1, engage2)
        print(n, c1, c2, engage1, engage2)

while engage1 or engage2:
    print(f'===============================Дополнительная итерация=====================================')
    if engage1 and 1 in clients:
        print('Сработал случай 2')
        t = t1
        engage1 = False
        c1 += 1
        Nd += 1
        if n == 1 or n == 2:
            print('Условие: n == 1 or n == 2')
            n -= 1
            t1 = float('inf')
            print(f'Клиент {clients.index(1) + 1} закончил обслуживаться')
            clients[clients.index(1)] = 4
            print(n, c1, c2, engage1, engage2)
        elif n > 2:
            n -= 1
            print(f'Клиент {clients.index(1) + 1} закончил обслуживаться')
            clients[clients.index(1)] = 4
            if list(map(lambda x: x > time_end, Di1)).count(True) == 0:
                engage1 = True
                y1 = service_func()
                t1 = t + y1
                Vi1.append(round(y1, 3))
                Di1.append(round(t1, 3))
                print(f't1 = {t1}')
                print(f'Клиент {clients.index(3) + 1} начал обслуживаться')
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 1
        print(n, c1, c2, engage1, engage2)

    if engage2 and 2 in clients:
        print('Сработал случай 3')
        engage2 = False
        t = t2
        c2 += 1
        Nd += 1
        if n == 1 or n == 2:
            n -= 1
            t2 = float('inf')
            print(f'Клиент {clients.index(2) + 1} закончил обслуживаться')
            clients[clients.index(2)] = 4
            print('Условие: n == 2')
            print(n, c1, c2, engage1, engage2)
        elif n > 2:
            n -= 1
            print(f'Клиент {clients.index(2) + 1} закончил обслуживаться')
            clients[clients.index(2)] = 4
            if list(map(lambda x: x > time_end, Di2)).count(True) == 0:
                engage2 = True
                y2 = service_func()
                t2 = t + y2
                Vi2.append(round(y2, 3))
                Di2.append(round(t2, 3))
                print(f't2 = {t2}')
                print(f'Клиент {clients.index(3) + 1} начал обслуживаться')
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 2
        print(n, c1, c2, engage1, engage2)
    if not engage1 and not engage2 and n > 0:
        print(f'Так и не были принято {n} клиентов')
        while 3 in clients:
            Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - time_end, 3))
            Si.append(round(Wi[clients.index((3))], 3))
            clients[clients.index(3)] = 4

result = [Ai, Di1, Di2, Vi1, Vi2, Wi, Si]

print(f'Na = {Na}, Nd = {Nd}')

print(f'''Приходов:{len(result[0])} {result[0]}
Обслуживание 1: {len(result[3])} {result[3]}
Обслуживание 2: {len(result[4])} {result[4]}
Уходы 1: {len(result[1])} {result[1]}
Уходы 2: {len(result[2])} {result[2]}
Лист ожиданий: {len(result[5])} {result[5]}
Время в системе: {len(result[6])} {result[6]}

''')


sc = sum(Si)/len(Si)

wd = sum(Wi)/len(Wi)

Wc = list(map(lambda y: 0 if y == 0 else 1, Wi))
wc = sum(Wc)/len(Wc)

qc = sum(Si)/(time_end - time_start)

ec = sum(Vi1)/(time_end - time_start) + sum(Vi2)/(time_end - time_start)

vc = (sum(Vi1)/len(Vi1) + sum(Vi2)/len(Vi2)) / 2

print(f'''=========Оценки за 1 день=========:
    Для клиентов:
    Среднее время клиента в системе: {round(sc, 5)}
    Средняя задержка клиентов в очереди: {round(wd, 5)}
    Среднее число клиентов в очереди: {round(wc, 5)}
    Ожидаемое число клиентов в очереди: {round(qc, 5)}
    Для устройств:
    Среднее время обслуживания: {round(vc, 5)}
    Оценка занятости устройств: {round(ec, 5)}''')
