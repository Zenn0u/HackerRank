# Enter your code here. Read input from STDIN. Print output to STDOUT

num, den = map(int, input().split())
n = int(input())

p = num/den
q=1-p
prob=1-q**n

print(round(prob,3))