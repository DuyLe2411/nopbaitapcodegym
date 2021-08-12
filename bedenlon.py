def sort_numbers(num1,num2,num3):
    temp = 0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    if num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return (num1, num2, num3)

x = int(input("Nhập số đầu: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ 3: "))
a, b, c = sort_numbers(x, y, z)
print("Original numbers: ", x,y,z)
print("Fixed numbers: ", a , b, c)

