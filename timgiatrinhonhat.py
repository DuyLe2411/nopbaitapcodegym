numbers = [1, 67, 100, 2112, 242, 22, 353]
def smallest_number(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result

print("Chuỗi số của bạn là: ", numbers)

print("Số nhỏ nhất trong chuỗi là: > ", smallest_number(numbers))
