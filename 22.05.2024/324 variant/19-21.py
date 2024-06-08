def f(s1: int, s2: int, k: int, win: list) -> int:
    if s1 + s2 >= 665: return k in win
    if k == max(win): return 0
    moves = [f(s1 + 3, s2, k + 1, win), f(s1, s2 + 3, k + 1, win), f(s1 * 4, s2, k + 1, win), f(s1, s2 * 4, k + 1, win)]
    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        # return any(moves) for 19 task
        return all(moves)


for s in range(1, 635 + 1):
    # if f(27, s, 0, [2]):
    #     print(s)
    # if f(27, s, 0, [1]) == 0 and f(27, s, 0, [3]) == 1:
    #     print(s)
    if f(27, s, 0, [2, 4]) == 1 and f(27, s, 0, [4]) == 0:
        print(s)