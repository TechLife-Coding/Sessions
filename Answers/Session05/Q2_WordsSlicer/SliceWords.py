words = input('type: ')
result = ''

for chrslice in words:
    if chrslice not in result:
        result+=chrslice

print(result)