

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
           writer.writerow(["Name", "Age", "Contact Number", "E-mail ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
       
       student_info = input("Enter student information for student #{}: in the following format(Name Age Contact_number Email_ID) ".format(student_num))
       print("Entered information :" + student_info)

         #split
       student_info_list = student_info.split(' ')

       print("\n Entered information is : \n Name:{} \n Age:{} \n Contact_number{} \n E-Mail_ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

       choice_check= input("Is the entered information correct? (Yes/No) :")

       if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter (Yes/No) if you want to enter information for another student: ")
       if condition_check == "yes":
                condition = True
                student_num = student_num + 1
       elif condition_check == "no":
                condition = False
       elif choice_check == "no":
                print("\n Please re-enter the values !")
             







