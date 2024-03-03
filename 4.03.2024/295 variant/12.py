def f(s: str) -> str:
    str = s
    while '12' in str or '21' in str:
        if '12' in str:
            str = str.replace('12', '21', 1)
        else:
            str = str.replace('21', '111', 1)
    return str


print(min([n for n in range(2, 150, 2) if f('21' * n).count('1') > 100]) * 2)