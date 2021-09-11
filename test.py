def project():
    total_of_invest = 0
    total_of_profit = 0
    z = 0
    while len(p_i) > 0:
        total_of_invest += c_i[z]
        if total_of_invest >= S:
            break
        c_i.pop(z)
        total_of_profit += p_i[z]
        p_i.pop(z)
    return total_of_profit
def largest_number(lst):
    largest = 0
    for i in range(len(lst)):
        if largest < lst[i]:
            largest = lst[i]
    return largest

n, S = map(int, input("Nhập số và vốn nào: ").split(' '))
c_i = []
p_i = []
for i in range(n):
    c_i.append(int(input((f"Nhập vốn cần tiêu {i+1}: "))))

for num in range(n):
    p_i.append(int(input((f"Nhập lợi nhuận nhận được {num+1}: "))))
list_profit = []

while len(p_i) > 0:
    list_profit.append(project())

print("Tổng lợi nhuận lớn nhất là: ",largest_number(list_profit))

        