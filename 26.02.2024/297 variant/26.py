f = open('source/26.txt')
s, n = map(int, f.readline().split())
books = [int(x) for x in f]
rare_books = [x for x in books if x > 3000]
simple_books = [x for x in books if x <= 3000]
rare_books.sort()
simple_books.sort()
print(simple_books)
s -= sum(rare_books[:3])
sum_of_simple_books = []
for i in range(len(simple_books)):
    if sum(sum_of_simple_books) + simple_books[i] < s:
        sum_of_simple_books.append(simple_books[i])

sum_of_simple_books.pop(len(sum_of_simple_books)-1)

for i in range(len(simple_books) - 1, -1, -1):
    if sum(sum_of_simple_books) + simple_books[i] < s:
        sum_of_simple_books.append(simple_books[i])
        break

print(len(sum_of_simple_books)+3, sum_of_simple_books[len(sum_of_simple_books)-1])