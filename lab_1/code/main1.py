import workWithArr
import moduleSort


def main():
    arr = []
    comp = swaps = 0
    size, arr_type, sort_type, leng = workWithArr.config()

    if arr_type == 'r':
        arr = workWithArr.rand_arr(size)
    elif arr_type == 's':
        arr = workWithArr.sorted_arr(size)
    elif arr_type == 'i':
        arr = workWithArr.inverse_arr(size)

    if leng != 0:
        print('\nNot sorted array:')
        workWithArr.print_arr(arr, leng)

    if sort_type == 'b':
        arr, comp, swaps = moduleSort.bubble_sort(arr)
    elif sort_type == 'c':
        arr, comp, swaps = moduleSort.comb_sort(arr)

    if leng != 0:
        print('\nSorted array:')
        workWithArr.print_arr(arr, leng)
    print('\nNumber of comparisons:', comp)
    print('Number of swaps:', swaps)


if __name__ == '__main__':
    main()
