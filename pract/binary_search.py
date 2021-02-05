def binary_search(lst, n):

    l = 0
    u = len(lst)-1

    while l <= u:
        mid = (l+u)//2

        if n == lst[mid]:
            return mid

        elif n > lst[mid]:
            l = mid+1

        else:
            u = mid-1

lst = [10, 30, 60, 80]
n = 90

print(binary_search(lst, n))