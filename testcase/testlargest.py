def largest(x,y,z):
   if (check_int_float(x) and check_int_float(y) and check_int_float(z)):
      if (x >= y) and (x >= z):
         t = x
      elif (y >= x) and (y >= z):
         t = y
      else:
         t = z
      return t

   else:
      return "Error"

def check_int_float(x):
   if (type(x) == int or type(x) == float):
      return True
   else:
      return False