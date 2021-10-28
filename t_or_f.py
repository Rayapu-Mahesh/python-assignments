def validateuser(name):
    if (name == 'mahesh'):
        return True
    else:
        return False
name=input("enter the name:")
print(validateuser(name))