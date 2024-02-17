def binary_search(num, first, last):
    global mid
    while first <= last:
        mid = first + (first + last)//2
        if list[mid] == num:
            return mid
        elif num < list[mid]:
            last = mid - 1
        else:
            if num > list[mid]:
                first = mid + 1
    return -1

list = [1, 3, 4, 5, 7, 8, 9, 11, 12, 15]
num = 1
first = list[0]
last = list[len(list) - 1]
result = binary_search(num, first, last)

if result == -1:
    print("There's no match")
else:
    print("The number is at index ", result)
print('Name')
