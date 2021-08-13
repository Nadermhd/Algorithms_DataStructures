# Push/pop operation Big O(1)
# search element in stack Big O(n)
# List can be used as stack (not efficient)
# collections.deque (recommended)
# Stack (LIFO) .append

from collections import deque
stack = deque()
stack.append([1])
stack.append([2])
stack.append([3])
print(stack)
print(stack.pop())

####################################
# Qeue (FIFO) .appendleft
q = deque()
q.appendleft([1])
q.appendleft([2])
q.appendleft([3])
print(q)
print(q.pop())