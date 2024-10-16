num_student = int(input())
student = list(map(int, input().split()))
order = []

for i in range(num_student):
    order.insert(len(order) - student[i], i + 1)

print(*order)

"""
다른 풀이
출력을 뒤집으면 더 간단하고 빠르다
"""

# num_student = int(input())
# student = list(map(int, input().split()))
# order = []
#
# for i in range(num_student):
#     order.insert(student[i], i + 1)
#
# print(*order[::-1])