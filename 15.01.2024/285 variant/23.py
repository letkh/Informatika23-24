def f(x,y,fl):
    if x > y+1:
        return 0
    if x == y:
        return 1
    if fl == 0:
        return f(x - 1, y, 1) + f(x * 2, y, 0) + f(x * 3, y, 0)
    if fl == 1:
        return f(x * 2, y, 0) + f(x * 3, y, 0)
    
print(f(3, 20, 0))