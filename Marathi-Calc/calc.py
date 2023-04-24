output = 0
num1 = ""
operation = ""
num2 = ""
num1 = input('''
**************************************************
Simple Calculator Developed by Ashutosh Palhare 
**************************************************

Pahila number tak\n''')
operation = input("kay karaychay te sang (+, -, *, /)?\n")

num2 = input("Ata Dusra number Tak\n")

floatnum1 = float(num1)
floatnum2 = float(num2)

if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
    print("Ghe tuz Answer : "+str(output))
else:
    print("Eka time la ekach kam sang na GayBanya")
