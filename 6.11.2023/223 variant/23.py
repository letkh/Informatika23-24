def f(s, f, m_count = 0):
    if (s > f) or (m_count > 3):
        return 0
    if s==f:
        return 1
    return f(s + 2, f, m_count) + f(s * 3, f, m_count + 1) + f(s * 5, f, m_count + 1)
 
print(f(1,300))