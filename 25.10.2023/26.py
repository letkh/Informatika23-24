
f = open("source/26.txt")
n = int(f.readline())
start_time = 1633305600
end_time = start_time + 604800
count = 0
time_process = [0 for i in range(0, 604801)]
for i in f:
    start_process, end_process = i.split()
    if (int(start_process) < start_time) and ((int(end_process) > start_time) or (int(end_process) == 0)):
        count = count + 1
    if (int(start_process) >= start_time) and (int(start_process) <= end_time):
        time_process[int(start_process) - start_time] = time_process[int(start_process) - start_time] + 1
    if (int(end_process) >= start_time) and (int(end_process) <= end_time):
        time_process[int(end_process) - start_time] = time_process[int(end_process) - start_time] - 1
sum_time = 0
max_process = 0
for i in range(1, 604801):
    count = count + time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time = sum_time + 1
print(max_process, sum_time)