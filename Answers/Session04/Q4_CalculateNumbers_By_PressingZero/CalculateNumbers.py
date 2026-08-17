sum1=0
for _ in range (1,101):
    numbers=float(input('enter number: '))
    sum1+=numbers
    if numbers==0:
        print(sum1)
        break
