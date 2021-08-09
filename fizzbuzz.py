startnum, endnum = input("Nhập vào 2 số bắt đầu , kết thúc: ").split()
startnum = int(startnum)
endnum = int(endnum)
if startnum > endnum:
    print("Khong co gia tri")
else:
    for number in range(startnum, endnum + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    

