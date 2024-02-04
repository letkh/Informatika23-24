def f(s, k, win):
    if s >= 21:
        return k in win
    if k == max(win):
        return 0
    moves = [f(s+1, k+1, win), f(s*2, k+1, win)]
    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 21):
    if f(s,0,[1]) == 0 and f(s,0,[3]) == 0 and f(s, 0, [1, 3, 5]) == 1:
        print(s)