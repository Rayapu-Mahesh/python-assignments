#age of 100 using function

name = str(input("What is your name: "))
age = int(input("How old are you: "))

def dob():
    year = (2021+(100-age))
    return year


print(name,"your age will become 100 in the year ",dob())