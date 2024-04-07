def f(s, k, win):
    if s >= 376:
        return k in win
    if k == max(win):
        return 0
    moves = [f(s + 2, k+1, win), f(s + 5, k + 1, win), f(s * 6, k + 1, win)]
    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 376):
    if f(s, 0, [2]) == 1:
        print('19:', s)
    if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
        print('20:', s)
    if f(s, 0, [2]) == 0 and f(s, 0, [2, 4]) == 1:
        print('21:', s)