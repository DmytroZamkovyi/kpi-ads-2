import random


# Display array
def print_arr(arr, size):
    for i in range(size):
        print(arr[i], end='')
        if i != size - 1:
            print(', ', end='')
        if i % 20 == 19 or i == size - 1:
            print("\n", end='')


# Create sorted array
def sorted_arr(size):
    return list(range(1, size + 1))


# Create inverse array
def inverse_arr(size):
    temp = list(range(1, size + 1))
    temp.reverse()
    return temp


# Create random array
def rand_arr(size):
    return random.sample(range(1, size + 1), size)


# Initial settings
def config():
    print('Array size',
          '================================================',
          'Use positive number',
          '================================================', sep='\n')
    size = input('Enter size: ')
    while not size.isdigit() or int(size) <= 0:
        print('ERROR:Invalid value')
        size = input('Enter number greater than 0: ')
    size = int(size)
    print('\nFill array',
          '================================================',
          '\'r\' - to fill array with random numbers',
          '\'s\' - to fill array with sorted numbers',
          '\'i\' - to fill array with inverse numbers',
          '================================================', sep='\n')
    arr_type = input('Enter method of filling array: ')
    while arr_type != 'r' and arr_type != 's' and arr_type != 'i':
        print('ERROR:Invalid value')
        arr_type = input('Enter method of filling array: ')
    print('\nSorting',
          '================================================',
          '\'b\' - sort array by bubble sort',
          '\'c\' - sort array by comb sort',
          '================================================', sep='\n')
    sort_type = input('Enter a sort method: ')
    while sort_type != 'b' and sort_type != 'c':
        print('ERROR:Invalid value')
        sort_type = input('Enter a sort method: ')
    print('\nOutput array',
          '================================================',
          'Use positive numbers to output n numbers of array',
          'Use 0 to no output array ',
          '================================================', sep='\n')
    leng = input('Enter how many numbers to output from the array: ')
    while not leng.isdigit() or int(leng) < -1 or int(leng) > size:
        print('ERROR:Invalid value')
        leng = input(f'Enter number greater than -1 and less than {size}: ')
    leng = int(leng)
    return size, arr_type, sort_type, leng
