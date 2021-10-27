#largest no among 3 using function

x = int(input("please enter an integer-1:"))
y = int(input("please enter an integer-2:"))
z = int(input("please enter an integer-3:"))

def largest():
   if (x >= y) and (x >= z):
      t = x
   elif (y >= x) and (y >= z):
      t = y
   else:
      t = z
   return t


print("the largest num is: ",largest())
