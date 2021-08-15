'''
Bubble sort algorithm
Bio O(n^2)
'''

def bubble_sort(arr):
    size = len(arr)

    for i in range(size-1):
        swapped = False # this variable is to check for a sorted array
        for j in range(size-1-i):

            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped = True
                
        if not swapped:
            break

    return arr

def bubble_sort_dict(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            # this is new 
            a = elements[j][key]
            b = elements[j+1][key]
            # end
            
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    arr = [12, 2, 4, 111, 98, 100, 19, 44, 66]
    print(bubble_sort(arr)) 

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort_dict(elements, key='transaction_amount')
    print(elements)