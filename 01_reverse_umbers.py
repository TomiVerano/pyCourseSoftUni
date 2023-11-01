import collections
from collections import deque

line = collections.deque(input().split())
line.reverse()
print(*line)
