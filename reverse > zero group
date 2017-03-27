Provided Input
100020300001
Expected Output
4

xs = raw_input()
max_count = 0
count = 0
for x in xs:
    if x == '0':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print max_count
