'''
Linear search algorithm
Bio O(n)
'''

def linear_search(arr, val):

    for i in range(len(arr)):
        if arr[i] == val:
            return i

if __name__ == '__main__':
    arr = [13, 6, 7, 18, 9, 4, 66, 8]
    print(linear_search(arr, 66))