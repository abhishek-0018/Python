def isprime(t):
     i=1
     c=0
     while i<=t//2:
          if t%i==0:
               c=c+1
               if c>2:
                    return 0
          else:
               i=i+1
     return 1
               

def oper(*a):
    if len(a)==1:
         u=a[0]
         y=1
         while u!=0:
              y=y*u
              u=u-1
         print(y)
         return
    elif len(a)==2 :
         t=a[1]
         b=a[0]
         c=a[1]
         while t!=0:
              d=b+c
              print(b)
              b=c
              c=d
              t=t-1
    else :
         s=a[2]
         if s!="Prime":
              print("Third argument is not valid")
              return
         else:
              r=a[0]-1
              d=a[1]
              while r<=d:
                   r=r+1
                   if isprime(r)==1:
                        print(r)

                   
oper(5)
oper(2,9)
oper(1,9,"Prime")

