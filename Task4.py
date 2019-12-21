num = int(input("Hour:"))
num1 = int(input("Min:"))
num2 = int(input("Sec:"))
num3 = int(input("Hour2:"))
num4 = int(input("Min2:"))
num5 = int(input("Sec2:"))

result = (((num - num3) * 3600) + ((num1 - num4) * 60) + (num2 - num5))
print(abs(result))
