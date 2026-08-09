newrec=0
oldrec=0
howhigh=0
for _ in range(10):
    jumper=float(input(('M /CM Jump:')))
    newrec=jumper
    if newrec > oldrec:
        howhigh= newrec - oldrec
        print(f'job well done you jump {howhigh} M higher this time')
    elif newrec == oldrec:
        print(f'old record was {oldrec} and new record is {newrec} same record try harder ')
    elif newrec < oldrec:
        howhigh = newrec - oldrec
        print(f'you jump {howhigh} M less this time')

    oldrec=newrec



