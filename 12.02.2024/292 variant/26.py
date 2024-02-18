f = open('source/26-10.txt') # подгрузка файла
n = f.readline() # количество цилиндров
a = [int(x) for x in f] # сами цилиндры в массиве
a.sort(reverse=True) # сортировка по убыванию
radius_now = a[0] # самый большой радиус, с которого будем начинать отсчет
c = 1 # наш счетчик цилиндров, берем 1, с которого начинаем
# цикл, в котором будем проверять, чтобы последующие цилиндры были больше на 7 единиц
for i in range(1,len(a)):
    if radius_now - a[i] >= 7: # само условие
        radius_now = a[i] # наш новый радиус
        c += 1 # новый цилиндр
print(c, radius_now)