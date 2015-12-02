# Enter your code here. Read input from STDIN. Print output to STDOUT

ladders = []
snakes = []
# testcases = raw_input()
l = int(raw_input())
for i in range(l):
    ladders.append(tuple([int(i) for i in raw_input().split(" ")]))
print ladders
s = int(raw_input())
for i in range(s):
    snakes.append(tuple([int(i) for i in raw_input().split(" ")]))

print snakes