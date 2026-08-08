full_name=input('enter name and famiy: ')
first_letter=full_name[0]
space=full_name.find(' ')
last_name=full_name[space + 1:]
print(f'{first_letter}.{last_name}')
