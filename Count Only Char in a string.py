
import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
message = message.lower()
result = re.sub('[^a-z]','', message)
print(len(result))
