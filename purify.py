def purify(list):
    new_list = []
    for i in list:
        if i % 2 == 0: new_list.append(i)
    return new_list

print (purify([1,2,2,4,5,5,7]))
