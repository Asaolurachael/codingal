# sum of first number for the given input
# Approach number one

def fun1(n):
    return n*(n+1)/2
print(fun1(4))

#(4*5)/2

#Approach number two

def fun2(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum

print(fun2(4))

#1+2+3+4

#Approach number three

def fun3(n):
    sum=0
    for i in range(1, n+2):
        for j in range(1, i+1):
            sum+=1
    return sum
print(fun3(4))

#1 = (1+1) + (1+1+1)+(1+1+1+1)