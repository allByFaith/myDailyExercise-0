wanted=input("enter 'c' for Cel and 'f' for Fah: ")
inTemp = int(input("enter a temperature to convert: "))

if (wanted == 'c'):
    result = (inTemp * 1.8 + 32)
    print(f"convert {inTemp}C to Fahrenheit : ", result, "F")
elif (wanted =='f'):
    result = (inTemp - 32) * (5/9)
    print("convert {inTemp}F to Celsius : ", result,  "C")
else:
    print('only c or f will be accepted for convertion!!!')

