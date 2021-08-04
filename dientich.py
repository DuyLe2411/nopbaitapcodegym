import math
a = float(input("Nhập độ dài cạnh thứ nhất của tam giác: "))
b = float(input("Nhập độ dài cạnh thứ hai của tam giác: "))
c = float(input("Nhập độ dài cạnh thứ ba của tam giác: "))
d = (a+b+c)/2
e = math.sqrt(d*(d-a)*(d-b)*(d-c))
print(f"Diện tích của tam giác là: {e}")
