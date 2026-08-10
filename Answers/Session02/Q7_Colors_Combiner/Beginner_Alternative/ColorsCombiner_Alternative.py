colors = []
for _ in range(1,4):
    colors.append(input('Choose Color: '))

if len(set(colors)) == 1:
    print('Three Color Same')
elif len(set(colors)) == 2:
    print('Two Color Same')
else:
    print('No Color Are The Same')
    