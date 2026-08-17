length=''
for _ in range(1,7):
    str1=input('enter str: ')
    length= len(str1) 
    if length %2 == 0 :
        print(str1[:length // 2])
    elif length % 2 != 0 :
        print(str1[length // 2 :])
        