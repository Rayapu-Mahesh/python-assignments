#largest no among 3 using var argument

def largest(*no):

 if (no[0] >= no[1]) and (no[0] >= no[2]):
  return no[0]
 elif (no[1] >= no[0]) and (no[1] >= no[2]):
  return no[1]
 else:
  return no[2]


print("the largest no is ", largest(10,20,30))
