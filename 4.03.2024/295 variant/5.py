# def f(n1: int, n2: int) -> [int, int]:
#     cond1 = int(str(n1)[0]) + int(str(n2)[0])
#     cond2 = int(str(n1)[1]) + int(str(n2)[1])
#     cond3 = int(str(n1)[2]) + int(str(n2)[2])
#     return [int(f'{cond3}{cond1}{cond2}'), int(f'{cond3}{cond1}{cond2}'[-4:-1])]
#
#
# print(max([x for x in range(100, 1000) for y in range(100, 1000) if f(x, y)[1] == 2]))

print(max([x for x in range(100, 1000) for y in range(100, 1000) if int(f'{int(str(x)[2]) + int(str(y)[2])}{int(str(x)[0]) + int(str(y)[0])}{int(str(x)[1]) + int(str(y)[1])}'[-4:-1]) == 2]))