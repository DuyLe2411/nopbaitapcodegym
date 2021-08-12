#Ghi danh sách các item hiện có(tên, tiền, ngày mua)
#def: add_item, find_item, remove_item
#Đưa ra 2 option add or remove
#Sử dụng if elif else để thưc hiện lệnh option

expenses = [
        {"Name":"Foods", "Cost":12000, "Date":"12/12/2021"},
        {"Name": "Taxi", "Cost":30000, "Date":"12/12/2021"}
]

def add_item(expenses, item):
        expenses.append(item)

def find_item(expenses, item_name):
        result = -1
        for i in range(len(expenses)):
                if expenses[i]['Name'] == item_name:
                        result = i
        return result

def remove_item(expenses, item_name):
        index = find_item(expenses, item_name)
        if index > -1:
                del expenses[index]
        else:
                print(item + "not in list")

print("Your expenses:  ", expenses)

print("What do you want to do?\n\
        1. Add\n\
        2. Remove")

choice = int(input("Select option 1 or 2: "))

name_input = input("Your item: ")

if choice == 1:
        cost_item = float(input("The price of your item: "))
        date_item = input("The date you buy it: ")
        item = {"Name":name_input, "Cost": cost_item, "Date": date_item}
        add_item(expenses, item)
        print("Your expenses: ", expenses)
elif choice == 2:
        remove_item(expenses, name_input)
        print("Your expenses: ", expenses)
else:
        print("Invalid system")