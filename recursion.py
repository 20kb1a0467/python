def func(n):
    if n>0:

        func(n%2)
        func(n//2)
    print(n)
n=int(input())
func(n)
