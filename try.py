x=10
'''def fun():
    x=20
    print("Value of x is",x)
fun()
print("Now val is",x)
def fun1(list1):
    list1[0]=100
    print(list1)
    print(id(list1))
list2=[1,2,3,4]
fun1(list2[:])#[:] this will transfer val of list
print("List=",list2)
print(id(list2))
try:
    # a=int(input("Enter a number"))
    # b=int(input("Enter a number"))
    a=8
    b=0
    c=a/b
    print(c)
except:
    print("Exception")'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4])
y=x*2
plt.plot(x,y)
plt.show()