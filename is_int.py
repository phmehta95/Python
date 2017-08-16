def is_int(x):
  if abs(x - round(x)) > 0:
  	return False
  else:
    return True


print (is_int(7.36))
print(is_int(8))
print(is_int(789.5))
