account=500
remaining=0
for _ in range(1,11):
    
    withraw=float(input('deposit price: '))

    print('----------------------------------------------------')
 
    if withraw > account:

        print('you have to charge your account first')
        print('----------------------------------------------------')
        chargeacc=float(input('amount of charge: '))
        if chargeacc <=0 or chargeacc < 5:

            print('withrawal failed!!')
   
        elif account < chargeacc:
            account=chargeacc
            print('----------------------------------------------------')
            print(f'deposited successfuly {account}$ to your account')
            print('----------------------------------------------------')
        elif withraw <=0:
            print('only positive numbers and numbers higher than Zero')   
    elif withraw <=0:
            print('only positive numbers and numbers higher than Zero') 
    elif withraw <= account :
       remaining = withraw 
       account -= remaining  
       print(f'wihraw sucessfuly amount of {remaining : .2f}$ remaining money is {account: .2f}$' )
       print('----------------------------------------------------')

        
       


