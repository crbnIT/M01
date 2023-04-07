# Corbyn Eaker
# M02Lab.py
# This app recieves a first name, last name and GPA from the user and gives information based on these inputs

# created variable to control the main loop and began main loop
running = True
while running:

    # ask user for last name and check to see if it is the exit trigger, exit program if so
    lastName = input("Enter a last name(enter 'zzz' to exit): ").title()
    if lastName.upper() == "ZZZ":
        print("Goodbye")
        running = False

    # have user fill out student's information after confirmed that they are continuing
    # filter responses starting the upper bound of weighted GPAs and descending, created an else to catch negative GPAs
    else:
        firstName = input("Enter a first name: ").title()
        gpa = float(input("Enter the student's GPA: "))
        if gpa >= 5.4:
            print(f"{firstName} {lastName} is a liar")
        elif gpa >= 3.5:
            print(f"{firstName} {lastName} has made the dean's list with a GPA of {gpa}")
        elif gpa >= 3.25:
            print(f"{firstName} {lastName} has made honor roll with a GPA of {gpa}")
        elif gpa >= 0:
            print(f"{firstName} {lastName} has a GPA of {gpa} and does not qualify")
        else:
            print("How did you get a negative GPA?")
