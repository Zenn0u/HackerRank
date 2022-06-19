# Enter your code here. Read input from STDIN. Print output to STDOUT

num, den = map(int, input().split())
n = int(input())

p = num/den
q = 1 - p

s=(q**(n-1))*p
s=round(s,3)
print(s)