a = (1, 2, 3, 4, 5)
b = ('one', 'two', 'three', 'four', 'five')
c = (1, 2.0, 'three', '4.0', 5, 6, 7)

print('a =', a)
print('b =', b)
print('c =', c)
print()

d = a+b
print('a+b =', d)
e = 3*c
print('3*c =', e)
print()

for i in c:
	print(i*3)

f = (a, b, c, 'hello')

for row in f:
	for col in row:
		print(col, end=' ')
	print()

