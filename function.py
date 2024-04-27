def gmean(a,b):
    mean=(a*b)/(a+b)
    return mean
def average(a=9,b=1):
    print("Average is: ",(a+b)/2)
def printalpha (abc_list, num_list):
 for char in abc_list:
    for num in num_list:
        print(char, num)
 return
printalpha (['a', 'b', 'c'], [1, 2, 3])
x=3
y=8
p=gmean(x,y)
print(p)

average()    # give average of 9,1
average(2,8)  # give average of 2,8
average(5)    # give average of 5,1
average(b=3)  # give average of 9,3
average(b=1,a=9)  # in function a=9, b=1