def f(s1: int, s2:int, k: int, win: list) -> int:
    if s1 * s2 >= 144:
        return k in win
    if k == max(win):
        return 0
    moves = [f(s1 + 1, s2, k + 1, win), f(s1 * 2, s2, k + 1, win), f(s1, s2 + 1, k + 1, win), f(s1, s2 * 2, k + 1, win)]

    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        # return any(moves) ДЛЯ 19
        return all(moves)


for s in range(1, 142):
    for m in range(1, 5):
        if f(1, s, 0, [m]) == 1:
            if m == 2:
                print('19: ', s)
            break
    if f(1, s, 0, [1]) == 0 and f(1, s, 0, [3]) == 1:
        print('20: ', s)
    if f(1, s, 0, [2]) == 0 and f(1, s, 0, [2,4]) == 1:
        print('21: ', s)