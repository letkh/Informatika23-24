s = open('source/24.txt').readline()
s = s.split()
a = [len(x) for x in s]
print(max(a))