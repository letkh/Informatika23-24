s = str(open('source/24.txt').readline())
s = s.split('000')
print(len(max(s, key=len)) + 4)