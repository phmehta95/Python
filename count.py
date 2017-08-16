def count(sequence,item):
	sum = 0
	for i in sequence:
 		if i == item:
   			sum += 1
	return sum


print (count([1,2,3,2,2,4,5,6,7,2],2))
