def remove_duplicates(list):
  new_list=[]
  for i in list:
    if i not in new_list:
      new_list+= [i]
  return new_list

print (remove_duplicates([1,1,2,2,3,3,4,5,6,6,7,8,8,9]))
