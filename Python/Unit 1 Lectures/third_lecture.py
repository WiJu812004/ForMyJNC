print('---------------')
print(False == 0)
print(False !=0)

print('---------------')
print('apple' < 'bee')
print("apple" < "app")
print('apple' <= 'apple')

print('---------------')
print(1 < 2)
print(1 != 5/7)
print(1 != 8/7)

print('---------------')
x, y = 16, 24
print(not(x%12 and y%12))
print(not x%12 and not y%12)
print(not x%12 or not y%12)

print('---------------')
G = int(input('Enter raw grade: '))
if G<60:
	upg = '5.00'
elif G>=60 and G<64:
	upg = '3.00'
elif G>=64 and G<68:
	upg = '2.75'
elif G>=68 and G<72:
	upg = '2.50'
elif G>=72 and G<76:
	upg = '2.25'
elif G>=76 and G<80:
	upg = '2.00'
elif G>=80 and G<84:
	upg = '1.75'
elif G>=84 and G<88:
	upg = '1.50'
elif G>=88 and G<92:
	upg = '1.25'
else:
	upg = '1.00'
print('UP grade equivalent is', upg)

print('---------------')
count = 0
nbin = 12
count += 100 # count = count + 1
nbin /= 2
print("after", count, nbin)

print('---------------')
# while loop
n = 1
while n<=10:
    print(n)
    n += 1
# for loop
for n in range(1,10):
    print(n)
	
print('---------------')
m = int(input("m = "))
n = int(input("n = "))
c = 0
while c < m:
   c += 1
   print(n*c)
for c in range(1, m+1):
   print(n*c)

print('---------------')
m = int(input("m = "))
n = int(input("n = "))

for i in range(m):
	for j in range(n):
		print("*", end="\t")
		j += 1
	print()
	i += 1
	