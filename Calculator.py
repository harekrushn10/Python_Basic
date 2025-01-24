num1 = float(input("Enter an First number: "))
sign = input("Enter and sign from(+ , - , * , / , // , % ,**): ")
num2 = float(input("Enter an Second number: "))

if sign == "+":
    total = num1 + num2
    print(f"Your sumation of {num1} {sign} {num2} is : {total}" )

elif sign == "-":
    sub = num1 + num2
    print(f"Your substraction of {num1} {sign} {num2} is : {sub}")

elif sign == "*":
    mul = num1 * num2
    print(f"Your multiplication of {num1} {sign} {num2} is : {mul}")

elif sign == "/":
    div = num1 / num2
    print(f"Your division of {num1} {sign} {num2} is : {div}")

elif sign == "//":
    fdiv = num1 // num2
    print(f"Your Floor division of {num1} {sign} {num2} is : {fdiv}")
    
elif sign == "%":
    mod = num1 % num2
    print(f"Your modulo of {num1} {sign} {num2} is : {mod}")

elif sign == "**":
    pow = num1 ** num2
    print(f"Your power of {num1} {sign} {num2} is : {pow}")

else:
    print("Enter valid oprator(+ , - , * , / , // , % ,**).")
    