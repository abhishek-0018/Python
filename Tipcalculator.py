total=input("Enter total amout:")
t=float(total)
people=input("Enter number of people you want to split you bill among:")
p=int(people)
tipper=input("Enter tip percent:")
tp=int(tipper)
amount=t+(tp/100*t)
indi=amount/p
#indi=round(indi,2)
indi="{:.2f}".format(indi)
print("Each person will give ",indi)
print(f"Your Amount was {t} and there were {p} peoples and tip was {tp}")