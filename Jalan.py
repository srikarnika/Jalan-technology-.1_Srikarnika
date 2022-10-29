#sorting of array in python
def rearrange(arr, n):
     temp = n*[None]
 

    small, large = 0, n-1
 
    flag = True
 

    for i in range(n):

        if flag is True:

            temp[i] = arr[large]

            large -= 1

        else:

            temp[i] = arr[small]

            small += 1
 

        flag = bool(1-flag)
 

    for i in range(n):

        arr[i] = temp[i]

    return arr
 

arr = [2,4 ,6 ,8 ,10]

n = len(arr)

print("Original Array")

print(arr)

print("Modified Array")

print(rearrange(arr, n))
