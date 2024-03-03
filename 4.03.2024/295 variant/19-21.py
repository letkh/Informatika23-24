def f(x1, x2, k, win):
    if x1 >= 479 or x2 >= 479:
        return k in win
    if k > max(win):
        return False
    moves = [f(x1 + 1, x2, k + 1, win), f(x1, x2 + 1, k + 1, win), f(x1 + 3, x2, k + 1, win), f(x1, x2 + 3, k + 1, win),
             f(x1 * 2, x2, k + 1, win), f(x1, x2 * 2, k + 1, win)]

    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 479):
    if f(239, s, 0, [1]) == 0 and f(239, s, 0, [2]) == 1:
        print('#19', s)
    if f(239, s, 0, [1]) == 0 and f(239, s, 0, [3]) == 1:
        print('#20', s)
    if f(239, s, 0, [2]) == 0 and f(239, s, 0, [2,4]) == 1:
        print('#21', s)