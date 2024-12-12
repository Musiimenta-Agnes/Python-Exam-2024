def student_details():
    student_name = 'Gloria Arinda'
    student_number = 'SEP23/DSC/088U/F'
    programming = 90
    data_science = 87
    computer_applications = 77


    average_mark = programming + data_science + computer_applications / 3
    print(f" The average mark of the student is: {average_mark:.3f}")

student_details()