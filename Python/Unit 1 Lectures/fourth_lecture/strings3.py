a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "mississippi"

print("a =", a)
print("a.count('A')", a.count('A'))
print("a.count('a')", a.count('a'))
print("a.lower()", a.lower())
print("a.lower().count('b')", a.lower().count('b'))
print()

print("b =", b)
print("b.count('s')", b.count('s'))
print("b.count('is')", b.count('is'))
print("b.index('si')", b.index('si'))
print()

for i in b:
	print(i)

for i in a:
	print(chr(ord(i)+1), end=' ')
print()

