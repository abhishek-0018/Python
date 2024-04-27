x=int(input("Enter a number: "))
match x:
    case _ if x%2==0:
        print(x," is a even number")
    case _ :
        print(x," is a odd number")