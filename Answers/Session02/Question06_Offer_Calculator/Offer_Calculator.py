calculate=float(input('buying price: '))
offer=0
if calculate > 1000000:
    offer = (calculate * 0.15)
    final_price= calculate - offer
    print(f'Offer: {offer}\nFinal price: {final_price}')
elif 500000<=calculate <=1000000:
    offer= (calculate * 0.1)
    final_price= calculate - offer
    print(f'Offer: {offer}\nFinal Price: {final_price}')
elif 100000 <= calculate <=499999:
    offer=0
    final_price= calculate
    print('Thers no Offer for You')
