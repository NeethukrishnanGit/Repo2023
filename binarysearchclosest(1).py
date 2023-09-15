def binarysearch(list,target):
    start=0
    end=len(list)-1
    while start<=end:
        mid=(start+end)//2
        if list[mid]==target:
            return mid
        if list[mid]>target:
            end=mid-1
        elif list[mid]<target:
            start=mid+1


    if(abs(list[max(mid-1,0)]-target)<abs(list[mid]-target)):
        return max(mid-1,0)

    if (abs(target-list[min(mid+1,len(list)-1)]))<abs(list[mid]-target):
        return min(mid+1,len(list)-1)
    return mid


num=[10,23,45,67,87,90]
target=int(input())
print(binarysearch(num,target))
