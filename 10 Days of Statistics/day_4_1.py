# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

def binom(n, k, p):
    b = (factorial(n)/(factorial(k)*factorial(n-k)))*(p**k)*((1-p)**(n-k))
    return(b)

n = 6    
p = 1.09/2.09
b = 0

for i in range(3,7):
    b += binom(n, i, p)
    
print("%.3f" %b)