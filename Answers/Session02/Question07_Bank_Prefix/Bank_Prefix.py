Bank_details={
     
     '6219':'Blue Bank',
     '5022':'Pasargad Bank',
     '5041':'Resalat Bank',
     '6037':'Saderat Bank',
     '5859':'Tejarat Bank',
     '5894':'Refah Bank',
     '6104':'Melat Bank',
     '6362':'Ayandeh Bank',
     '5047':'Shahr Bank',
     '6221':'Parsian Bank'
     
     }
prefix=input('BANK ACC: ')
first_numbers=prefix[:4]
if first_numbers in Bank_details:
    print(f'{Bank_details[first_numbers]}: {first_numbers}')
