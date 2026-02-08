def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

print("LCM =", lcm(X, Y))