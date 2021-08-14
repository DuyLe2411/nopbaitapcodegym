import random as r
numbers = []
for i in range(r.randint(1,11)):
    num = r.randint(0,500)
    numbers.append(num)

numbers.sort()
print("List numbers là: ", numbers)
print("Số lớn nhất và lớn thứ hai trong chuỗi số là: ", str(numbers[-1])+ ' và ' + str(numbers[-2]))
if len(numbers) < 2:
    print("List này không thể có số lớn nhất và số lớn thứ hai do số lượng trong list")
    print("Số lớn nhất là: ", numbers[-1])