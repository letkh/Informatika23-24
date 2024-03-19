s = str(open('source/24.txt').readline())
s = s.split('00')
print(len(max(s, key=len)) + 2)