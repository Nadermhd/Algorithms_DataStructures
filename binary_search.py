'''
Binary search algorithm
Bio O(log n)
'''

def binary_search(arr, val):
    start = 0
    end = len(arr) -1
    
    # Move the cursor (start and end) until they match
    while start <= end:
        mid_indx = (start + end) // 2
        mid_num = arr[mid_indx]

        if mid_num == val:
            return mid_indx

        if mid_num < val:
            start = mid_indx + 1
        else:
            end = mid_indx + 1
    return -1

def binary_search_recursion(arr, val, start, end):

    if end < start:
        return print('Num does not exist')

    mid_indx = (start + end) // 2

    if mid_indx >= len(arr)  or mid_indx < 0:
        return print('Num does not exist')

    mid_num = arr[mid_indx]

    if mid_num == val:
        return mid_indx

    if mid_num < val:
        start = mid_indx + 1
    else:
        end = mid_indx + 1
    return binary_search_recursion(arr, val, start, end)


if __name__ == '__main__':
    arr = [1, 2, 4, 18, 19, 44, 66, 98, 100]
    print(binary_search(arr, 98))
    print(binary_search_recursion(arr, 19, 0, len(arr)))