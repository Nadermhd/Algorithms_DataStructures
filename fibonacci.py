
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

print(fibo(15))
for i in range(10):
    print(fibo(i))