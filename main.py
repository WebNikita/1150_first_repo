def my_sum(**kwargs):
    
    print(kwargs)
    return 0

my_sum(name = "Test", age = 16, weight = 34, school = 1123)

summa = lambda *args: sum(args)

print(summa(1,2,3,4,5))