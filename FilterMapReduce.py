# filter() is used to filter out iterables.eg we are given a list 
# of numbers and we need to find all the even numbers.

nums  = [1,2,4,5,3,23,12,7,9,11,24,16]
even = list(filter(lambda x : x%2==0,nums))
print(even)

# map() is used to apply particular operation to all the elements. eg if we want to double all the 
# elements of even list.

double = list(map(lambda x : x*2,even))
print(double)

# The reduce() function accepts a function and a sequence and returns a single value.Eg if we want 
# to find the sum or mean of a list

from functools import reduce

addition = reduce(lambda a,b:a+b,double)
avg = reduce(lambda a,b:(a+b)/2,double)

print(addition,avg)