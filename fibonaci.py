
def sum(a, b):
    return a + b


def fib(n):
    assert n >=0 and int(n)==n, 'Invalid parameter! Must be grater then 0 and integer!'
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return sum(fib(n-2), fib(n-1))
    
def main():

    for x in range(1,30):
       print(str(fib(x)))
 
if __name__ == '__main__':
    main()