# count = int(input())
#
# for i in range(count):
#     a, b = map(int, input().split())
#
#     print(a + b)

import sys

data = list(map(int, sys.stdin.read().split()))
result = list()

for i in range(1, data[0]*2+1, 2):
    result.append(str(data[i] + data[i + 1]))

sys.stdout.write('\n'.join(result))