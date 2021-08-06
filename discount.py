cash = float(input("Bạn đã tiêu bao nhiêu tiền: "))
if  cash < 75 and cash > 0:
    print("Oops, you can't get a discount.")
elif cash >= 75:
    print("you will get a discount")
    print("Total price you have to pay is: ", cash - 15)
elif cash >= 100:
    print("you will get a discount")
    print("Total price you have to pay is: ", cash - 25)
elif cash >= 150:
    print("you will get a discount")
    print("Total price you have to pay is: ", cash - 50)
else:
    print("Price must be greater than 0")
