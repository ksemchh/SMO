from functions import lambd, poisson_func, service_func
from prettytable import PrettyTable


time_start = 8
time_end = 9

Ai = []
Ai1 = []
Ai2 = []
AI = []
AI1 = []
AI2 = []
Di1 = []
DI1 = []
Di2 = []
DI2 = []
Vi1 = []
VI1 = []
Vi2 = []
VI2 = []
Si = []
Si1 = []
Si2 = []
SI = []
SI1 = []
SI2 = []
Wi = []
Wi1 = []
Wi2 = []
WI = []
WI1 = []
WI2 = []
Na = 0
NA = []
Nd = 0
ND = []
Ni1 = []
Ni2 = []
NI1 = []
NI2 = []
n = 0
c1 = 0
c2 = 0
engage1 = False
engage2 = False
counter = 0
clients = []

for i in range(1, 2):
    tA = poisson_func(time_start)
    t1 = float('inf')
    t2 = float('inf')
    while tA < time_end:
        counter += 1
        if tA < t1 or tA < t2:
            Ai.append(round(tA, 3))
            clients.append(0)
            t = tA
            Na += 1
            Tt = poisson_func(t)
            while not Tt:
                Tt = poisson_func(t)
            tA = Tt
            if engage1 == False and engage2 == False:
                y1 = service_func(lambd)
                t1 = t + y1
                n += 1
                engage1 = True
                Ai1.append(round(t, 3))
                Ni1.append(clients.index(0) + 1)
                Di1.append(round(t1, 3))
                Vi1.append(round(y1, 3))
                Si.append(round((t1 - t), 3))
                Si1.append(round(t1 - t, 3))
                Wi.append(0)
                Wi1.append(0)
                clients[clients.index(0)] = 1
            elif engage1 == False and engage2 == True:
                y1 = service_func(lambd)
                t1 = t + y1
                n += 1
                engage1 = True
                Ai1.append(round(t, 3))
                Ni1.append(clients.index(0) + 1)
                Di1.append(round(t1, 3))
                Vi1.append(round(y1, 3))
                Si.append(round((t1 - t), 3))
                Si1.append(round(t1 - t, 3))
                Wi.append(0)
                Wi1.append(0)
                clients[clients.index(0)] = 1
            elif engage1 == True and engage2 == False:
                y2 = service_func(lambd)
                t2 = t + y2
                n += 1
                engage2 = True
                Ai2.append(round(t, 3))
                Ni2.append(clients.index(0) + 1)
                Di2.append(round(t2, 3))
                Vi2.append(round(y2, 3))
                Si.append(round((t2 - t), 3))
                Si2.append(round(t2 - t, 3))
                Wi.append(0)
                Wi2.append(0)
                clients[clients.index(0)] = 2
            elif engage1 == True and engage2 == True:
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
                    Ai1.append(round(Wi[clients.index((3))], 3))
                    Ni1.append(clients.index(3) + 1)
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Wi1.append(Wi[clients.index((3))])
                    Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                    Si1.append(round(t1 - t + Wi[clients.index((3))], 3))
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
                    Ai2.append(round(Wi[clients.index((3))], 3))
                    Ni2.append(clients.index(3) + 1)
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Wi2.append(Wi[clients.index((3))])
                    Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                    Si2.append(round(t2 - t + Wi[clients.index((3))], 3))
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
                    Ai1.append(round(Wi[clients.index((3))], 3))
                    Ni1.append(clients.index(3) + 1)
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Wi1.append(Wi[clients.index((3))])
                    Si.append(round(t1 - t + Wi[clients.index((3))], 3))
                    Si1.append(round(t1 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 1
                    y1 = service_func()
                    t1 = t + y1
                    engage1 = True
                    Vi1.append(round(y1, 3))
                    Di1.append(round(t1, 3))

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
                    Ai2.append(round(Wi[clients.index((3))], 3))
                    Ni2.append(clients.index(3) + 1)
                    Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - t, 3))
                    Wi2.append(Wi[clients.index((3))])
                    Si.append(round(t2 - t + Wi[clients.index((3))], 3))
                    Si2.append(round(t2 - t + Wi[clients.index((3))], 3))
                    clients[clients.index(3)] = 2
                    y2 = service_func()
                    t2 = t + y2
                    engage2 = True
                    Vi2.append(round(y2, 3))
                    Di2.append(round(t2, 3))
        if not engage1 and not engage2 and n > 0:
            while 3 in clients:
                Wi[clients.index((3))] = abs(round(Wi[clients.index((3))] - time_end, 3))
                Si.append(round(Wi[clients.index((3))], 3))
                clients[clients.index(3)] = 4

    AI.append(Ai)
    AI1.append(Ai1)
    AI2.append(Ai2)
    DI1.append(Di1)
    DI2.append(Di2)
    VI1.append(Vi1)
    VI2.append(Vi2)
    WI.append(Wi)
    WI1.append(Wi1)
    WI2.append(Wi2)
    NA.append(Na)
    ND.append(Nd)
    SI.append(Si)
    SI1.append(Si1)
    SI2.append(Si2)
    NI1.append(Ni1)
    NI2.append(Ni2)
    Ai = []
    Ai1 = []
    Ai2 = []
    Di1 = []
    Di2 = []
    Vi1 = []
    Vi2 = []
    Wi = []
    Wi1 = []
    Wi2 = []
    Si = []
    Si1 = []
    Si2 = []
    Na = 0
    Nd = 0
    Ni1 = []
    Ni2 = []
    n = 0
    c1 = 0
    c2 = 0
    engage1 = False
    engage2 = False
    counter = 0
    clients = []

result = [AI, DI1, DI2, VI1, VI2, WI, SI, AI1, AI2, WI1, WI2, SI1, SI2, NI1, NI2]

print(f'''=========Результаты дня=========
Приходы: {len(result[0][0])}             {result[0][0]}
Лист ожиданий: {len(result[5][0])}       {result[5][0]}
Обслуживание 1: {len(result[3][0])}       {result[3][0]}
Обслуживание 2: {len(result[4][0])}       {result[4][0]}
Уходы 1: {len(result[1][0])}              {result[1][0]}
Уходы 2: {len(result[2][0])}              {result[2][0]}
Время в системе: {len(result[6][0])}     {result[6][0]}
''')

print('=========Первое устройство=========')

table1 = PrettyTable(['Клиент', 'Приход', 'Ожидание', ' Обслуживание', 'Уход', 'Время в системе'])
for i in range(len(result[13][0])):
    table1.add_row([result[13][0][i], result[7][0][i], result[9][0][i], result[3][0][i], result[1][0][i], result[11][0][i]])
print(table1)
print('=========Второе устройство=========')

table2 = PrettyTable(['Клиент', 'Приход', 'Ожидание', ' Обслуживание', 'Уход', 'Время в системе'])
for i in range(len(result[14][0])):
    table2.add_row([result[14][0][i], result[8][0][i], result[10][0][i], result[4][0][i], result[2][0][i], result[12][0][i]])
print(table2)

clients = {result[13][0][i]:(result[7][0][i], result[3][0][i]) for i in range(len(result[13][0]))} | {result[14][0][i]:(result[8][0][i], result[4][0][i]) for i in range(len(result[14][0]))}

sorted_clients = dict(sorted(clients.items()))

print('=========Таблица для верификации=========')
table3 = PrettyTable()
table3.add_column('№ Клиента', ['Время прибытия', 'Время обслуживания'])
for key, value in sorted_clients.items():
    table3.add_column(str(key), [str(value[0]), str(value[1])])
print(table3)

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
    print(f'''=========Оценка за {len(result[0])} день=========:
    Общие:
    Всего прибыло клиентов:              {len(result[0][0])}
    Было обслужено первым устройством:   {len(result[3][0])}
    Было обслужено вторым устройством:   {len(result[3][0])}
    Не было обслужено:                   {len(result[0][0]) - (len(result[1][0]) + len(result[2][0]))}
    Для клиентов:
    Среднее время клиента в системе:     {round(sc, 5)}
    Средняя задержка клиентов в очереди: {round(wd, 5)}
    Среднее число клиентов в очереди:    {round(wc, 5)}
    Ожидаемое число клиентов в очереди:  {round(qc, 5)}
    Для устройств:
    Среднее время обслуживания:          {round(vc, 5)}
    Оценка занятости устройств:          {round(ec, 5)}''')