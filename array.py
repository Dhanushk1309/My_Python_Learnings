# import bisect  
# a = [2, 4, 6, 8, 10]
# print(6 in a)       
# print(a.count(7) > 0)   
# pos = bisect.bisect_left(a, 8)   #bisect_left means returns the left_mot values
# print("Found at index:", pos)


# from array import *
# arr1=array('i',[1,2,3,4,5,6])
# arr2=arr1
# print(arr1.tolist())
# print(arr2)


# Print Alternates

# arr=[-5,2,0,1,4,1,3]
# res=[]
# for i in range(0,len(arr),2):
#     res.append(arr[i])
# print(res)
 
#  Print the leaders in a array

def leaders(arr):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                break
        else:
            res.append(arr[i])
    return res
arr=[16,17,2,3,5,4]
print("Leaders in the array are:",leaders(arr))
