
def firstRec(n):
    if n < 1:
        print('Koniec')
    else:
        print('wartość n: ' + str(n))
        firstRec(n-1)


def main():
    a = 'test'
    print(a)

    firstRec(1000)

if __name__ == '__main__':
    main()