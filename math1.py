import math
import random
print("""print(pow(2,3))
print(abs(4-9))
print(math.factorial(5))
print(math.ceil(3.4))
print(round(5.2))
print(random.random()*100)
print(random.choice(["Hello","ok","yes"]))
list=["Hello","Naruto","One piece"]
random.shuffle(list)
print(list)""")
def fun(a,b):
    return a+b
print(fun(2,3))
def fun1(*a):
    print(type(a))
    if len(a)==2:
        print("Two")
    elif len(a)==3:
        print("Three")
fun1(3)
fun1()
fun1(1,2,3)
