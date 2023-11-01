import collections
from collections import deque

children = input().split()
children_playing = collections.deque(children)
count_move = int(input()) - 1
while len(children_playing) != 1:
    children_playing.rotate(-count_move)
    print("Removed {0}".format(children_playing.popleft()))
print("Last is {0}".format(children_playing[0]))



