def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        f0 = 0
        f1 = 1
        fn = 0
        while n >= 2:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n -= 1
        return fn
n = -1
while n < 0:
    n = int(input("Nhap vao so tu nhien n: "))
    if(n>=0):
        break
result = fibonacci(n)
print(result)
