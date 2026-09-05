counter=0
errors=0
l=['@','!','?','%','#','$','&']
for i in range(10):
    password = (input('enter pass: '))
    counter+=1
    if len(password) < 8 :
        print('the pass must be 8 char at least')
        errors+=1
        print('-----------------------------------------')
    if password[0] != password[0].upper() :
        print('first letter must be Capitalize')
        errors+=1
        print('-----------------------------------------')
    if password[1:] != password[1:].lower():
        print('at least one lower word needed')
        print('-----------------------------------------')
    if not any (j.isdigit() for j in password):
        print('at least one number required')
        errors+=1
        print('-----------------------------------------')
    if not any(j in '@!$%&?#' for j in password):
        print('at least one special chr needed (@ !  ?  $  #  &  %)')
        errors+=1
    if errors == 0:
         print('valid password')
         