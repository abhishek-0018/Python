def my_grade(marks):
    if marks>=90:
        return 'A+'
    elif 80<=marks<90:
        return 'A'
    elif 70<=marks<80:
        return 'B+'
    elif 60<=marks<70:
        return 'B'
    elif 50<=marks<60:
        return 'C'
    elif 40<=marks<50:
        return 'D'
    else:
        return 'F'

def report_card(subjects):
    with open('report_card.txt', 'w') as file:
        file.write("Subject\t\tMM\t\n")
        file.write("\n")
        for subject, marks in subjects.items():
            grade=my_grade(marks)
            file.write(f"{subject}\t\t{marks}\t{grade}\n")

def main():
    subjects={}
    for i in range (3):
        subject=input(f"Enter subject {i+1} name: ")
        marks=float(input(f"Enter marks for {subject}: "))
        subjects[subject]=marks

    report_card(subjects)
    print("Report card generated successfully.")

if __name__=="__main__":
    main()