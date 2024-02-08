def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
def partition(arr,start,end):
    pivot_index=start
    pivot=arr[pivot_index]
    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start+=1
            print(start)
        while arr[end]>pivot:
            end-=1
        if start<end:
            swap(arr,start,end)
    swap(arr,pivot_index,end)
    return end
    
def quick_sort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quick_sort(arr,start,pi-1)
        quick_sort(arr,pi+1,end)
def main():
    list1=[6,7,8,9,4,3]
    quick_sort(list1,0,len(list1)-1)
    print(list1)
if __name__=="__main__":
    main()
    
