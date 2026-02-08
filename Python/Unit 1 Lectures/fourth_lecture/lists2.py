a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print('len(a) =', a)
print('a =', a)
for i in range(len(a)):
	a[i] += 3
print()

print('a =', a)
print('a[2:4] =', a[2:4])
print('a[:-3] =', a[3:])
print('a[::-1] =', a[::-1])
print()

del(a[1])
print('del(a[1]):', a)
a.pop(4)
print('a.pop(4): ', a)
a.remove(9)
print('a.remove(15): ', a)
a.append('hamburger')
print("a.append('hamburger'): ", a)
print('a.index(21) = ', a.index(21))
print()

print('a.index(12) = ', a.index(12))
if 12 in a:
	print('a.index(12) = ', a.index(12))
else:
	print("Not in list")
a.append(12)
if 12 in a:
	print('a.index(12) = ', a.index(12))
else:
	print("Not in list")
