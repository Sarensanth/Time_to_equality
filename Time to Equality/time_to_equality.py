def equal(array):

    maxi=-float('inf')
    for i in array:
        if maxi<i:
            maxi=i

    time=0
    for i in array:
        time+=maxi-i
    
    return time

array=list(map(int,input().split()))
print(equal(array))
