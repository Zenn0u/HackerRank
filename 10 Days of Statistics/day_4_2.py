# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

def binom(n, k, p):
    b = (factorial(n)/(factorial(k)*factorial(n-k)))*(p**k)*((1-p)**(n-k))
    return(b)

p, n = list(map(int, input().split(" ")))
print(round(sum([binom(n, i, p/100) for i in range(3)]), 3))
print(round(sum([binom(n, i, p/100) for i in range(2, n+1)]), 3))