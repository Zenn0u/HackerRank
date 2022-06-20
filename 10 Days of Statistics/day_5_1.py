# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import exp, factorial

x_mean = float(input())
value = int(input())

poisson = ((x_mean ** value) * exp(-x_mean)) / factorial(value)
print("%.3f" %poisson)