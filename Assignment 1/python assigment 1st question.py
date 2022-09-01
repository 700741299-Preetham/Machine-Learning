import math
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

#sorting and finding max and min element
ages.sort()
print(ages)
print("the smallest element is : ",min(ages))
print("the largest element is : ",max(ages))


#adding the max and min element to list
ages.append(19)
ages.append(26)
print("After adding min and max ages : ",ages)

#finding the median
res = statistics.median(ages)
print("Median of the list is :", str(res))

#finding average
Average = sum(ages) / len(ages)
print("Average of the list is :" , str(Average))

#finding range
print("Range of list is : ", (max(ages)-min(ages)))