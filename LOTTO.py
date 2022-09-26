import random
import time
am = 6
tot = 49
y = 1
mojeliczby = []

print("ZABAWMY SIĘ W SYMULATOR LOTTO. PAMIĘTAJ WPISYWAĆ TYLKO LICZBY Z PRZEDZIAŁU 1-49")
for i in range(am):
    print('Podaj swoją', y, 'liczbę: ')
    a = int(input())
    mojeliczby.append(a)
    y += 1

start = time.perf_counter()
wygr = random.sample(range(tot+1), am)

x = 0
while True:
    ilosc = dict()
    if len(set(mojeliczby) & set(wygr)) == 6:
        print('Twoje liczby wylosowano za:', x, 'razem')
        print(mojeliczby)
        print(wygr)
        break
    else:
        x = x+1
        wygr = random.sample(range(tot+1), am)
end = time.perf_counter()
print('Komputer musiał losować przez:', end-start, 'sekund')
