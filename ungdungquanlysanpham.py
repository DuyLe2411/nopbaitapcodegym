products_db = {
101: 'QUYT',      
102: 'XOAI',      
103: 'CAM',      
104: 'BUOI',      
105: 'TAO',      
106: 'MIT'
}

#Lập hàm tìm sản phẩm
#Lập hàm cập nhật sản phẩm
#Cho chạy hàm while tới khi nào chọn exit thì break
#Chia 4 trường hợp if...elif.. với add, remove, update, exit//// trường hợp còn lại báo hệ thống lỗi
#Sau mỗi lần tác động thì in list ra


print("Your products:\n " ,products_db)
#Hàm lấy ID của sản phẩm trong list
def get_product_info(products_db, id_prod):
    if id_prod in products_db:
        return products_db[id_prod]

#Hàm thêm tên sản phẩm cho ID 
def update_info(products_db, id_prod, name_prod):
    products_db[id_prod] = name_prod

while True:
    
    print("""What do you want to do?
    1. Add
    2. Update
    3. Remove
    4. Exit""")

    choice = int(input("Number u will choose: "))
#ADD
    if choice == 1:
        product_id = int(input("Choose your ID product:  "))
        get_product_info(products_db, product_id)
        if product_id in products_db:
            print("Product with ID {", product_id, ' : ', get_product_info(products_db,product_id), "} already exists.")
        else:
            product_name = input("Choose your product's name: ")
            update_info(products_db,product_id,product_name)
            print("Your products:\n " ,products_db)
#UPDATE
    elif choice == 2:
        product_id = int(input("Choose your ID product:  "))
        if get_product_info(products_db,product_id):
            product_new_name =  input("Choose your product's new name: ")
            update_info(products_db,product_id,product_new_name)
            print("Your products:\n " ,products_db)
        else:
            print("Product with ID",product_id, " doesnt exists.")
#REMOVE
    elif choice == 3:
        product_id = int(input("Choose your ID product:  "))
        if product_id in products_db:
            del products_db[product_id]
            print("Your products:\n " ,products_db)
        else:
            print("Product with ID",product_id, " doesnt exists.")
    elif choice == 4:
        break
    else:
        print("Invalid input")



