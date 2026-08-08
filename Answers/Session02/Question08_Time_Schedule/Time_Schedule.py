for _ in range(10):
    time=input('Enter Time (HH:MM): ')
    hour,minute= time.split(':')
    hour= int(hour)
    minute= int(minute)
    if hour < 0 or hour >23 or minute <0 or minute >59:
        print('Inavalid Time!!?')
    else:
        if 0 <= hour <5:
            period_time='Night'
        elif 5 <= hour < 12 :
            period_time='Morning'
        elif 12 <= hour < 17:
            period_time='Afternoon'
        elif hour < 21:
            period_time = 'Evening'
        else:
            period_time('Night')

        if hour == 0:
            display_hour= 12
            am_pm='AM'
        elif hour <12 :
            display_hour= hour
            am_pm='AM'
        elif hour == 12:
            display_hour= 12
            am_pm='PM'
        else:
            display_hour = hour -12
            am_pm='PM'

        print(f'{display_hour} : {minute:02d} {am_pm} ({period_time})')
