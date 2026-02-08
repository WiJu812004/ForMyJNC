def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

N = int(input("Enter N: "))

count = 0
num = 2
while count < N:
    if prime(num):
        print(num, end=" ")
        count += 1
    num += 1
