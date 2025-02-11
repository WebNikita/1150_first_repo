def func_1(x):
    if x % 2 == 0:
        return True
    else:
        return False

def func_2(x):
    return x % 2 == 0

func_3 = lambda x: x % 2 == 0

def func_4(list_a, list_b):
    return list(set(list_a) & set(list_b))


count = func_1(2)

print(count)

def factorial(n):
    count = 1
    for i in range(2, n + 1):
        count *= i
    return count

# def factorial(n):
#     print(n)
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7))