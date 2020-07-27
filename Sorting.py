def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

def insertion(arr):
    for i in range(1,len(arr)):
        j = i - 1
        x = arr[i]
        while(arr[j]>x and j >-1):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = x
    print(arr)

def selection(arr):
    for i in range(len(arr)-1):
        j=k=i
        while(j<len(arr)):
            if arr[j] < arr[k]:
                k=j
            j+=1
        arr[i],arr[k] =arr[k],arr[i]
    print(arr)

def quick(arr):
    arr.append(float('inf'))
    


l = [7,2,5,2,0,1,10,-2]

bubble(l)



insertion(l)


selection(l)


