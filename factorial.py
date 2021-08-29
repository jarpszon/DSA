def factorial(n):
    assert n >=0 and int(n)==n, 'Invalid parameter! Must be grater then 0 and integer!'
    if n < 2:
        return n
    else:
        return n * factorial(n-1)

def main():
    print(str(factorial(-10)))


if __name__ == '__main__':
    main()