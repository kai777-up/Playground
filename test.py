def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(5))
a = [1, 1, 2, 3, 5]