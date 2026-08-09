sum1=0
value1=0
value2=0
for i in range(10):
    number=float(input('enter number: '))

    if number % 2 == 0 :

        value1+=number*5
        
    elif number % 2 !=0 :

        value2+=number+5

sum1=(value1+value2)

print(sum1)