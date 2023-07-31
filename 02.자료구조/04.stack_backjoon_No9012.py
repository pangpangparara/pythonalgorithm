import sys

stack = []
n = int(input())

for i in range(n):
    a = sys.stdin.readline().split('(')
    print(a)
#    for j in range(len(a)):
#         print(j)
#         print(a[j])
#         if a[j] == '(':
#             stack.push(a[j])
#         elif a[j]== ')':
#             stack.pop(-1)  

