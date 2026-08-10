import subprocess
import math
sum1=0
for _ in range(100):
    number1=float(input('num1:'))
    print('assignments --> + - / // * % ** abs sqrt  abs&sqrt')
    assign=input('assignment :')
    number2=float(input('num2: '))
    subprocess.run('cls',shell=True)

    if assign.lstrip() == '+':
       sum1 = number1 + number2
       print(f'result: {sum1}')
    elif assign.lstrip() == '-':
        sum1 = number1-number2
        print(f'result: {sum1}')
    elif assign.lstrip() == '/':
        sum1 = number1 / number2
        print(f'result: {sum1}')
    elif assign.lstrip == '*':
        sum1 = number1 * number2
        print(f'result: {sum1}')
    elif assign.lstrip() == '**':
        sum1 = number1 ** number2
        print(f'result: {sum1}')
    elif assign.lstrip() == '//' :
        sum1 = number1 // number2
        print(f'result: {sum1}')
    elif assign.lstrip() == '%':
        sum1 = number1 % number2
    elif assign.upper().lstrip().replace(' ','') == 'SQRT':
        sum1 = math.sqrt(number1+number2)
        print(f'sqrt: {sum1}')
    elif assign.upper().lstrip().replace(' ','') == 'ABS':
        sum1 = abs(number1+number2)
        print(f'abs: {sum1}')
    elif assign.upper().strip().replace(' ','') == 'ABS&SQRT':
        sq=math.sqrt(abs(number1+number2))
        ab=abs(number1+number2)
        print(f'abs : {ab}  sqrt : {sq}')
        