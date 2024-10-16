#ask input for name (identify the student)
name=input("Please enter your name: ")
section=input("Please enter your section:")

#ask input for prelim, midterm, and finals grade using if else statement method to verify if user is inputing a grade >40 and <100
prelim_grade=float(input("Please input your Preliminary Grade: "))
if prelim_grade <40.0 or prelim_grade >100.0:
    print("ERROR: Please enter a preliminary grade between 40 and 100 only.")   
else:
    midterm_grade=float(input("Please input your Midterm Grade: "))
    if midterm_grade <40.0 or midterm_grade >100.0:
        print("ERROR: Please enter a midterm grade between 40 and 100 only.")
    else:
        finals_grade=float(input("Please input your Finals Grade: "))
        if finals_grade <40.0 or midterm_grade >100.0:
            print("ERROR: Please enter a midterm grade between 40 and 100 only.")
        else:
            #formula to be used in getting the raw percent grade, then rounding off to determine what is the gpa and status of the grade
            final_grade= (prelim_grade*0.3333) + (midterm_grade*0.3333) + (finals_grade*0.3333)
            final_rounded_grade= round(final_grade)
            print("Final Grade: ", final_rounded_grade)
            
            if final_rounded_grade>= 99 and final_rounded_grade<=100:
                grade= 1.0
                status= "Excellent!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 96 and final_rounded_grade<=98:
                grade= 1.25
                status= "Outstanding!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 93 and final_rounded_grade<=95:  
                grade= 1.50
                status= "Superior!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 90 and final_rounded_grade<=92:
                grade= 1.75
                status= "Very Good!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 87 and final_rounded_grade<=89:
                grade= 2.00
                status= "Good!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 84 and final_rounded_grade<=86:
                grade= 2.25
                status= "Satisfactory!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 81 and final_rounded_grade<=83:
                grade= 2.50
                status= "Fairly Satisfactory!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 78 and final_rounded_grade<=80:
                grade= 2.75
                status= "Fair!"
                print("GPA: ", grade,"=", status)
            elif final_rounded_grade>= 75 and final_rounded_grade<=77:
                grade= 3.0
                status= "Passed!"
                print("GPA: ", grade,"=", status)
            else:
                final_rounded_grade< 75
                grade= 5.0
                status= "Failed!"
                print("GPA: ", grade,"=", status)
        