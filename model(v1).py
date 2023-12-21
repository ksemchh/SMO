from functions import lambd, poisson_func, service_func

time_start = 8
time_end = 19

Ai = []
AI = []
Di1 = []
DI1 = []
Di2 = []
DI2 = []
Vi1 = []
VI1 = []
Vi2 = []
VI2 = []
Si = []
SI = []
Wi = []
WI = []
Na = 0
NA = []
Nd = 0
ND = []
n = 0
c1 = 0
c2 = 0
engage1 = False
engage2 = False
counter = 0
clients = []

for i in range(1, 1001):
    tA = poisson_func(time_start)
    t1 = float('inf')
    t2 = float('inf')
    while tA < time_end:
        if tA < t1 or tA < t2:
            Ai.append(round(tA, 3))
            clients.append(0)
            t = tA
            Na += 1
            Tt = poisson_func(t)
            while not Tt:
                Tt = poisson_func(t)
            tA = Tt
            if not engage1 and not engage2:
                y1 = service_func(lambd)
                t1 = t + y1
                n += 1
                engage1 = True
                Di1.append(round(t1, 3))
                Vi1.append(round(y1, 3))
                Si.append(round((t1 - t), 3))
                Wi.append(0)
                clients[clients.index(0)] = 1
            elif engage1 and not engage2:
                y2 = service_func(lambd)
                t2 = t + y2
                n += 1
                engage2 = True
                Di2.append(round(t2, 3))
                Vi2.append(round(y2, 3))
                Si.append(round((t2 - t), 3))
                Wi.append(0)
                clients[clients.index(0)] = 2
            elif not engage1 and engage2:
                y1 = service_func(lambd)
                t1 = t + y1
                n += 1
                engage1 = True
                Di1.append(round(t1, 3))
                Vi1.append(round(y1, 3))
                Si.append(round((t1 - t), 3))
                Wi.append(0)
                clients[clients.index(0)] = 1
            elif engage1 and engage2:
                n += 1
                Wi.append(t)
                clients[clients.index(0)] = 3

        if t1 < tA and t1 <= t2:
            t = t1
            engage1 = False
            c1 += 1
            Nd += 1
            if n == 1 or n == 2:
                n -= 1
                t1 = float('inf')
                clients[clients.index(1)] = 4
            elif n > 2:
                n -= 1
                y1 = service_func()
                t1 = t + y1
                clients[clients.index(1)] = 4
                if list(map(lambda x: x > time_end, Di1)).count(True) == 0:
                    engage1 = True
                    Vi1.append(round(y1, 3))
                    Di1.append(round(t1, 3))
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 1

        if t2 < tA and t2 <= t1:
            engage2 = False
            t = t2
            c2 += 1
            Nd += 1
            if n == 1 or n == 2:
                n -= 1
                t2 = float('inf')
                clients[clients.index(2)] = 4
            elif n > 2:
                n -= 1
                y2 = service_func()
                t2 = t + y2
                clients[clients.index(2)] = 4
                if list(map(lambda x: x > time_end, Di2)).count(True) == 0:
                    engage2 = True
                    Vi2.append(round(y2, 3))
                    Di2.append(round(t2, 3))
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 2

    while engage1 or engage2:
        if engage1 and 1 in clients:
            t = t1
            engage1 = False
            c1 += 1
            Nd += 1
            if n == 1 or n == 2:
                n -= 1
                t1 = float('inf')
                clients[clients.index(1)] = 4
            elif n > 2:
                n -= 1
                clients[clients.index(1)] = 4
                if list(map(lambda x: x > time_end, Di1)).count(True) == 0:
                    engage1 = True
                    y1 = service_func()
                    t1 = t + y1
                    Vi1.append(round(y1, 3))
                    Di1.append(round(t1, 3))
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 1

        if engage2 and 2 in clients:
            engage2 = False
            t = t2
            c2 += 1
            Nd += 1
            if n == 1 or n == 2:
                n -= 1
                t2 = float('inf')
                clients[clients.index(2)] = 4
            elif n > 2:
                n -= 1
                clients[clients.index(2)] = 4
                if list(map(lambda x: x > time_end, Di2)).count(True) == 0:
                    engage2 = True
                    y2 = service_func()
                    t2 = t + y2
                    Vi2.append(round(y2, 3))
                    Di2.append(round(t2, 3))
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 2
        if 1 not in clients and 2 not in clients and n > 0:
            while 3 in clients:
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - time_end, 3))
                Si.append(round(Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 4

    AI.append(Ai)
    DI1.append(Di1)
    DI2.append(Di2)
    VI1.append(Vi1)
    VI2.append(Vi2)
    WI.append(Wi)
    NA.append(Na)
    ND.append(Nd)
    SI.append(Si)
    Ai = []
    Di1 = []
    Di2 = []
    Vi1 = []
    Vi2 = []
    Wi = []
    Si = []
    Na = 0
    Nd = 0
    n = 0
    c1 = 0
    c2 = 0
    engage1 = False
    engage2 = False
    counter = 0
    clients = []

result = [AI, DI1, DI2, VI1, VI2, WI, SI]

print(f'''=========Результаты на первый день=========
Приходы:{len(result[0][0])} {result[0][0]}
Обслуживание 1: {len(result[3][0])} {result[3][0]}
Обслуживание 2: {len(result[4][0])} {result[4][0]}
Уходы 1: {len(result[1][0])} {result[1][0]}
Уходы 2: {len(result[2][0])} {result[2][0]}
Лист ожиданий: {len(result[5][0])} {result[5][0]}
Время в системе: {len(result[6][0])} {result[6][0]}
''')

Sc = list(map(lambda x: sum(x)/len(x), SI))
sc = sum(Sc)/len(Sc)

WId = list(map(lambda x: sum(x) / (len(x) - 1), WI))
wd = sum(WId)/len(WId)

WIc = list(map(lambda x: list(map(lambda y: 0 if y == 0 else 1, x)), WI))
Wc = list(map(lambda x: sum(x) / len(x), WIc))
wc = sum(Wc)/len(Wc)

Qc = list(map(lambda x: sum(x) / (time_end - time_start), SI))
qc = sum(Qc)/len(Qc)

Ec1 = list(map(lambda x: sum(x) / (time_end - time_start), VI1))
Ec2 = list(map(lambda x: sum(x) / (time_end - time_start), VI2))
ec = sum(Ec1)/len(Ec1) + sum(Ec2)/len(Ec2)

Vc1 = list(map(lambda x: sum(x) / len(x), VI1))
Vc2 = list(map(lambda x: sum(x) / len(x), VI2))
vc = (sum(Vc1)/len(Vc1) + sum(Vc2)/len(Vc2)) / 2

if __name__ == '__main__':
    print(f'''=========Оценки за {len(result[0])} дней=========:
    Для клиентов:
    Среднее время клиента в системе: {round(sc, 5)}
    Средняя задержка клиентов в очереди: {round(wd, 5)}
    Среднее число клиентов в очереди: {round(wc, 5)}
    Ожидаемое число клиентов в очереди: {round(qc, 5)}
    Для устройств:
    Среднее время обслуживания: {round(vc, 5)}
    Оценка занятости устройств: {round(ec, 5)}''')