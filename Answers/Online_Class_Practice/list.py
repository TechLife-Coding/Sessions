l1=[]
product=(input('do you want shopping!!?? :'))
if product.upper() or product.lstrip() == 'YES':
    l1.append(product)
    with open ('product.txt','a',encoding='utf-8') as pd:
        pd.write(product + '\n')
    print(l1)