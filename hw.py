i = 0 
k = int(input('Enter your number:'))
print('The numbers available are ', k, 'are:', end='')

def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return f(n-1) + f(n-2)
    
while f(i)<k:
    print(f(i), end='')
    i += 1  