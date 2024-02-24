def f(s):
    string = s
    while '00' not in string:
        string = string.replace('033', '1302', 1)
        string = string.replace('03', '120', 1)
        string = string.replace('023', '203', 1)
        string = string.replace('02', '20', 1)
    return string

print(f('0' + '3' * 362 + '32' * 152 + '2' * 334 + '0').count('3'))
# for dv in range(1, 1000):
#     for tr in range(1, 1000):
#         if f('0' + '2' * dv + '3' * tr + '0').count('1') == 333 \
#             and f('0' + '2' * dv + '3' * tr + '0').count('2') == 819 \
#             and f('0' + '2' * dv + '3' * tr + '0').count('3') == 181:
#             print(dv)