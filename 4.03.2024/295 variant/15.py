def f(a: int, b: int, x: int) -> bool:
    return a <= x <= b


for e in range(1, 100):
    if all((not f(15, 40, x * 0.25)) or (not ((not f(21, 63, x * 0.25)) and (not f(7, e, x * 0.25)))) or (not f(15, 40, x * 0.25)) for x in range(1, 1000)):
        print(e)


# for e in range(1, 100):
#     for x in [k * 0.25 for k in range(-10000, 10000)]:
#         A = 0
#         D = 15 <= x <= 40
#         C = 21 <= x <= 63
#         f = D <= ((not D) and (not A)) <= (not D)
#         if f != 1:
#             print(x)