import subprocess
for _ in range(100):
  way=float(input('fee per km: '))
  if  way < 2:
    taxifee= 20
    print(f'Distance: {way}Km')
    print(f'Taxi Fee : {taxifee}$')

  elif way >=2:
        feeplus=way-2
        subprocess.run('cls',shell=True)
        print(f'Distance: {way}Km')
        taxifee = 20 + (feeplus * 5)
        print(f'Taxi Fee: {taxifee}')

