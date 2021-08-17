def get_info_student(student_list, number):
     
        if number in student_list:
            return student_list[number] 
    
def update_info_student(student_list, number, kind_of_in4, student_in4):
        student_list[number][kind_of_in4] = student_in4

class Student:
    def __init__(self) :
        global students_list
        students_list = {1:{"ID":101,"Name":"Lê Quốc Duy","Date":"24/11/2003", "Place": "Đà Nẵng"},
                          2:{"ID":102,"Name":"Nguyễn Minh Triết","Date":"08/08/2003", "Place": "Đà Nẵng"},
                          3:{"ID":103,"Name":"Nguyễn Minh Hiệu","Date":"10/06/2003", "Place": "Đà Nẵng"},
                          4:{"ID":104,"Name":"Nguyễn Hoàng Khải","Date":"01/08/2003", "Place": "Đà Nẵng"},
                          5:{"ID":105,"Name":"Hồ Vũ Hùng","Date":"07/04/2003", "Place": "Đà Nẵng"}}
    
    

    
    def control_system(self,student_list):
        while True:
            print("Student list:\n " ,student_list, end='\n')

            print("""What do you want to do?
    1. Add
    2. Update
    3. Remove
    4. Search
    5. Sort
    6. Exit""")
            choice = int(input("1,2,3,4,5 or 6?: "))

#ADD
            if choice == 1:
                student_num = int(input("Pick a num: "))
                get_info_student(student_list,student_num)
                if student_num in student_list:
                    print("The student with ", student_num , " number already exists.")
                else:
                    
                    sort_of_in4 = input("ID, Name, Date or Place (Type correctly such as 'in4'): ")
                    student_in4 = input("Add what (Type correctly such as 'in4'): ")
                    update_info_student(student_list, student_num, sort_of_in4, student_in4)
                    print("Student list: \n", student_list)

#UPDATE
            elif choice == 2:
                student_num = int(input("Pick a num: "))
                if student_num in student_list:
                    
                    sort_of_in4 = input("ID, Name, Date or Place: ")
                    student_in4 = input("Add what: ")
                    update_info_student(self, student_list, student_num,sort_of_in4,student_in4)
                    print("Student list: ", student_list)
                else:
                    print("Student with that ", student_num, " doenst exists.")
#REMOVE
            elif choice == 3:
                student_num = int(input("Pick a num: "))
                if student_num in student_list:
                    decision = input("What do you want to remove, (number) or (kind of info) (type correctly the word): ")
                    if decision.lower() == "number":
                        del student_list[student_num]
                        print("Student list: ", student_list)
                    elif decision.lower() == "kind of info":
                        sort_of_in4 = input("ID, Name, Date or Place (Type correctly such as 'in4'): ")
                        del student_list[student_num][sort_of_in4]
                        print("Student list: ", student_list)
                    else:
                        print("ERROR")
                else:
                    print("Student with that ", student_num, " doenst exists.")

#SEARCH
            elif choice == 4:
                student_num = int(input("Pick a num: "))
                if student_num in student_list:
                    print(student_list[student_num])
                else:
                    print("Student with that ", student_num, " doenst exists.")

#SORT
            elif choice == 5:
                student_list.sort()
                print("Student list: ", student_list)
#EXIT
            elif choice == 6:
                break
            else:
                print("Invalid input")

S = Student()
S.control_system(students_list)


