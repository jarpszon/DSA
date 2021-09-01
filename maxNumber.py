def findMaxNum(sampleArray, n):
    if n==1:
        return sampleArray[0]
    return max(sampleArray[n-1], findMaxNum(sampleArray,n-1))

def main():

    r = [1,34,2345,535677,43,6546,555,7647,764,535]
    print(str(findMaxNum(r, 3)))


if __name__ == '__main__':
    main() 