'''''
def selection_sort(arr):
    for idx in range(len(arr)):
        min_val=arr[idx]
        min_idx=idx
        for j in range(idx+1,len(arr)):
            if arr[j]> min_val:

                min_val=arr[j]
                min_idx=j
        temp=arr[min_idx]
        arr[min_idx]=arr[idx]
        arr[idx]=temp
    return (arr)
my_list=[10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
sorted_numbers=selection_sort(my_list)
print(sorted_numbers)
'''

''''
numbers = [17, 3, 9, 21, 2, 7, 5]
print("Before:", numbers)

for index1 in range(0, len(numbers)-1):
   min_val = numbers[index1]
   min_index = index1

   for index2 in range(index1+1, len(numbers)):
    if numbers[index2] < min_val:
        min_val = numbers[index2]
        min_index = index2

    temp = min_val
    numbers[min_index] = numbers[index1]
    numbers[index1] = temp
print("After:", numbers)
'''
'''''
lst1 = []

n1 = int(input("Enter number of elements : "))
for i in range(n1):
    ele = int(input())
    lst1.append(ele)
print(lst1)
lst2=[]
n2 = int(input("Enter number of elements : "))
for i in range(n2):
    ele = int(input())
    lst2.append(ele)
print(lst2)
concate=(lst1+lst2)
print(concate)
def  bubble_sort(concate):
    for idx in range(len(concate)):
        min=concate[idx]
        min_idx=idx
        for j in range(idx+1,len(concate)):
            if concate[j]<min:
                min=concate[j]
                min_idx=j
        temp=concate[min_idx]
        concate[min_idx]=concate[idx]
        concate[idx]=temp
    return (concate)
n=bubble_sort(concate)
print("Sorted list is:",n)
import statistics
print("Median number is : % s "
      % (statistics.median(n)))
'''''

