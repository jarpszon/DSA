from array import *


def main():

# 1. Create array and traverse.
    print('\nStep1')
    my_array = array('i',[1,2,3,4,5])  
    for i in my_array:
         print(i)

# 2. pick value by index
    print('\nStep2')
    print(my_array[0])

# 3. add to array
    print('\nStep3')
    my_array.append(6)
    for i in my_array:
        print(i)

# 4. insert to array
    print('\nStep4')
    my_array.insert(2,123)
    for i in my_array:
        print(i)

# 5. extend array
    print('\nStep5')

    my_array1 = array('i',[123,124,125])
    my_array.extend(my_array1)
    for i in my_array:
        print(i)

        
if __name__ == '__main__':
    main()