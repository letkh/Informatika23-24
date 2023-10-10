k = 0
for x1 in 'ЕЛЙ':
    for x2 in 'ЕЛЙ':
        for x3 in 'ЕЛЙ':
            for x4 in 'ЕЛЙ':
                for x5 in 'ЕЛЙ':
                    for x6 in 'ЕЛЙ':
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != 'Й' and x6 != 'Й':
                            if not('ЙЕ' in s or 'ЕЙ' in s):
                                if s.count('Й') <= 1:
                                    k += 1
print(k)