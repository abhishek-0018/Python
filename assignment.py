m=[{"name":"aman","roll":123}]
while(True):
    print("""
          
          1. ADD New record
          2. SEARCH Record by roll
          3.EDIT Record by roll
          4.DELETE record by roll
          5.DISPLAY
          6.EXIT
          """)
    i=int(input("Enter your choice "))
    if(i==1):
        name=input("Enter the Name ")
        roll=input("Enter the Roll No. ")
        d={"name":name,"roll":roll}
        m.append(d)
    elif(i==2):
        r=int(input("Enter the roll"))
        f=0
        for i in m:
            if(i["roll"]==r):
                print(i["name"])
                f=1
                break
        if(f==0):
            print("NOT found")
    elif(i==3):
        r=int(input("Enter the roll"))
        f=0
        for i in m:
            if(i["roll"]==r):
                f=1
                n=input("Enter the New Name ")
                i["name"]=n
                break
        if(f==0):
            print("NOT found")
    elif(i==4):
       r=int(input("Enter the roll"))
       f=0
       for i in m:
        if(i["roll"]==r):
            m.remove(i)
            f=1
            print("Deleted")
            break
        if(f==0):
            print("NOT found")
    elif(i==5):
        print()
        for i in m:
            print(i)
    elif(i==6):
        break
    else:
        print("Invalid input ")