def isPrime(n):
    for i in range(2, n//2+1):
        if(n % i == 0):
            return False
        return True
n = int(input("Enter a number"))
for i in range(2, n+1):
    if(isPrime(i)):
        print(i)