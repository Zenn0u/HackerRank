# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_Prime(n):
    if divisors(n) == []:
        print("Prime")
    else:
        print("Not prime")
            
def divisors(n):
    d_list = []
    if n <= 1:
        d_list.append(1)
        return d_list
    
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            d_list.append(i)
            return d_list
    return d_list
    
if __name__ == '__main__':    
    int_n = int(input())
    
    for _ in range(int_n):
        n = int(input().strip())
        is_Prime(n)