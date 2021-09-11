def stick_number():
    lst = [x for x in input("Nhập số: ").split(" ")]
    sb = ''
    while len(lst) > 0:
        largest = str(0)
        for i in range(len(lst)):
            if largest < lst[i]:
                largest = lst[i]
        sb += largest
        lst.remove(largest)
    return sb
print(stick_number())