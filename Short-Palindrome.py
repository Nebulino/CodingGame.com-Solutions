

for i in range(int(input())):w=input();print('true')if w==w[::-1]else print('false')

or a better one:

for i in range(int(input())):w=input();print("true" if w==w[::-1] else "false")
