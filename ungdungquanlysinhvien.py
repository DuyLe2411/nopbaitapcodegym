def get_info_student(student_list, ID):
     
        if ID in student_list:
            return student_list[ID] 
    
def update_info_student(student_list, ID, kind_of_in4, student_in4):
        student_list[ID][kind_of_in4] = student_in4

def add_student(student_list, ID):
    Name = input("Name: ")
    Date = input("Date: ")
    Place = input("Place: ")
    items = {"Name":Name,"Date":Date,"Place":Place}
    student_list[ID] = items
    return student_list
class Student:
    def __init__(self) :
   
        self.students_list = {101:{"Name":"Lê Quốc Duy","Date":"24/11/2003", "Place": "Đà Nẵng"},
                          102:{"Name":"Nguyễn Minh Triết","Date":"08/08/2003", "Place": "Đà Nẵng"},
                          103:{"Name":"Nguyễn Minh Hiệu","Date":"10/06/2003", "Place": "Đà Nẵng"},
                          104:{"Name":"Nguyễn Hoàng Khải","Date":"01/08/2003", "Place": "Đà Nẵng"},
                          105:{"Name":"Hồ Vũ Hùng","Date":"07/04/2003", "Place": "Đà Nẵng"}}
    
    

    
    def control_system(self):
        while True:
            print('\n\n')
            print("\t\t\t\t\tStudent list: ")
            for i in range(len(self.students_list)):
                print(i+101,': ',self.students_list[i+101],end='\n')
            print("""What do you want to do?
    1. Add
    2. Update
    3. Remove
    4. Search
    5. Exit""")
    
            choice = int(input("1,2,3,4 or 5?: "))

#ADD
            if choice == 1:
                ID = int(input("Pick a ID: "))
            
                self.ID = ID
                
                if self.ID in self.students_list:
                    print("The student with ", self.ID , " ID already exists.")
                else:
                    add_student(self.students_list, self.ID)
                    
                    
                   
#UPDATE
            elif choice == 2:
                ID = int(input("Pick a ID: "))
            
                self.ID = ID
                if self.ID in self.students_list:
                    
                    sort_of_in4 = input("Name, Date or Place: ")
                    self.sort_of_in4 = sort_of_in4
                    student_in4 = input("Add what: ")
                    self.student_in4 = student_in4
                    update_info_student(self.students_list, self.ID, self.sort_of_in4, self.student_in4)
                else:
                    print("Student with that ", self.ID, " doenst exists.")
#REMOVE
            elif choice == 3:
                ID = int(input("Pick a ID: "))
                self.ID = ID
                if self.ID in self.students_list:
                    decision = input("What do you want to remove, (ID) or (kind of info) (type correctly the word): ")
                    if decision.upper() == "ID":
                        del self.students_list[ID]
                    elif decision.lower() == "kind of info":
                        sort_of_in4 = input("Name, Date or Place (Type correctly the word): ")
                        del self.students_list[ID][sort_of_in4]
                    else:
                        print("ERROR")
                else:
                    print("Student with that ", self.ID, " doenst exists.")

#SEARCH
            elif choice == 4:
                ID = int(input("Pick a ID: "))
                self.ID = ID
                if self.ID in self.students_list:
                    print(self.students_list[ID])
                else:
                    print("Student with that ", self.ID, " doenst exists.")
           
#EXIT
            elif choice == 5:
                break
            else:
                print("Invalid input")

S = Student()
S.control_system()


