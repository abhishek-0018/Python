def addition(a,b):
    if b==0:
        return a
    else:
        return addition(a+1,b-1)
a=2
b=9
print(addition(a,b))
#############
