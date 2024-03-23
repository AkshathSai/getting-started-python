
def factorialOfANumberRecursive(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1;
    else:
        return n * factorialOfANumberRecursive(n-1)
    
def factorialOfANumber(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial    

print(factorialOfANumberRecursive(5))    
print(factorialOfANumber(5))
