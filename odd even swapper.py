#! python3.6
# -*- coding='utf-8'

s = raw_input()
print ''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
