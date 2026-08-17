import random
rand=random.randint(1,100)
for _ in range(1,20):
    number=float(input('enter number: '))
    if number > rand :
        print('---------------------------------------')
        print('number is smaller than what you guess')
        print('---------------------------------------')
    elif number < rand:
        print('---------------------------------------')
        print('number is bigger than what you guess')
        print('---------------------------------------')
    elif number == rand:
        print('---------------------------------------')
        print('yey finaly you win congratulations')
        print('---------------------------------------')
        break