def fibonacci(n):
    a=0
    b=1
    fibo=[]
    while a<=n:
        fibo.append(a)
        a,b=b,a+b
    return fibo


