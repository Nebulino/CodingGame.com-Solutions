

string = ''
value_count = int(input())
for value in input().split():
    item = ''.join(chr(int(value[i:i+2], 16)) for i in range(0, len(value), 2))
    print(item, sep=' ', end='', flush=True)
