def factorial(n):
  if n < 2:
    return 1
  else: 
    return n * factorial(n-1)

print(factorial(5))

print("---------------------------------------")

def square_i(n):
    out = 0
    for i in range(n):
        out += n
    return out

y = square_i(4)

print(y)

print("---------------------------------------")

def square_i(n):
    out = 0
    for i in range(n):
        out += n
    return out

def square_l(n):
    out = square_i(n-1)
    out += n + n - 1
    return out

x = square_l(4)

print(x)

print("---------------------------------------")

def square_l2(n):
    out = square_l2(n-1)
    out += n + n - 1
    return out

def square_r(n):
    if n == 1:
        return 1
    out = square_r(n-1)
    out += n + n - 1
    return out

z = square_r(4)

print(z)

print("---------------------------------------")

def square_r(n):
    if n == 2:
        return 4
    out = square_r(n-1)
    out += n + n - 1
    return out

a = square_r(4)

print(a)

print("---------------------------------------")

def square(n):
    if n < 0:
        return square_r(-n)
    return square_r(n)	

def square_r(n):
    if n == 0:
        return 0
    out = square_r(n-1)
    out += n + n - 1
    return out

a = square(4)

print(a)

print("---------------------------------------")

def foo(n):							
    print("+", n)
    if n > 0:
        foo(n-1)
    print("-", n)

print(foo(4))

print("---------------------------------------")

def fib(n):						
    print("+", n)
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    print("-", n)

print(fib(7))

print("---------------------------------------")

def fib(n):						
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(10))

print("---------------------------------------")

def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)
    
print(fact_rec(7))

print("---------------------------------------")

def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(fact_iter(7))