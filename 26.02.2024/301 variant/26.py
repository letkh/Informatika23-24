f = open('source/26.txt')
n = int(f.readline())
a = [0]*n
info_scheme = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
departed = 0
for i in range(n):
    arrival_time, maintenance_time, window_number = map(int, f.readline().split())
    a[i] = [arrival_time, maintenance_time, window_number]
a.sort()
for i in range(n):
    arrival_time, maintenance_time, window_number = a[i][0], a[i][1], a[i][2]
    if info_scheme[window_number - 1][0] - arrival_time <= 40:
        info_scheme[window_number - 1][1] += 1
        info_scheme[window_number - 1][0] = max(arrival_time, info_scheme[window_number - 1][0]) + maintenance_time
    else:
        departed += 1

print(departed, info_scheme)