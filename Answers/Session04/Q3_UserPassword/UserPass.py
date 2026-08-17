for _ in range(1,11):
   print('Character Limit ( 8 )')
   print('first 4  Characters (Letters) Second 4  Characters (Numbers)')
  
   password = input('pass : ')
   if password[-4:].isdigit() and password==password[:8]:
    print('-----------------------')
    print('Password is Valid')
    print('-----------------------')
   elif password[-4:] != password.isdigit() and password > password[:8]:
     print('Pasword is Not Valid')
     print('-------------------------------------------------------')
     print('        The Password Should be Only 8 Characters        ')
     print('First 4 Characters (Letters) Second 4 Characters(Numbers)')
     print('-------------------------------------------------------')
