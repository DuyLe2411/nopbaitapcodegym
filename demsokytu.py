def count(string):
    result = 0
    for i in range(len(string)):
        result += 1
    return result

your_string = input("Nhập chuỗi của bạn: ")

print("Số ký tự trong chuỗi là: ", count(your_string))