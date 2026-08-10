colors=[]
for _ in range(1,4):
    color=input('Choose Color: ')
    colors.append(color)
if colors[0] == colors[1] ==colors[2]:
    print('three color same')
elif colors[0] == colors[1] or colors[0] == colors[2] or colors[1] == colors[2]:
    print('two color same')
else:
    print('none of them same')
    