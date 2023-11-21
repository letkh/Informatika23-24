nabor = 'алпця'
k = 0
for x1 in nabor:
    for x2 in nabor:
        for x3 in nabor:
            for x4 in nabor:
                for x5 in nabor:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if s.count('а') <= 1 and s.count('ц') == 2 and s.count('л') == 0:
                        print(k, s)
