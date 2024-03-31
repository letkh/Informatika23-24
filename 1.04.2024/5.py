def f(n: int) -> int:
    n2 = format(n, 'b')
    n2 = f'{n2}{str(sum(map(int, n2)) % 2)}'
    n2 = f'{n2}{str(sum(map(int, n2)) % 2)}'
    return int(n2, 2)

print(min([f(x) for x in range(1, 100) if f(x) > 43]))