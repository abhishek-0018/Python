class userException(Exception):
    "Failed because marks are less than 0"
    pass
total=0
for i in range (1,6):
    try:
        marks=int(input("Enter marks of an student "))
        if marks<0 or marks>100:
            raise userException
        char(input())
        else:
            print("Marks are",marks)
            total=total+marks
    except userException:
        print("Invalid marks")
print("Total marks obtained by a student are ",total)
