
from collections import namedtuple, deque
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

my_deque = deque([1, 2, 3])

# Add to the right side (end)
my_deque.append(4)
print(my_deque) # Output: deque([1, 2, 3, 4])

# Add to the left side (start)
my_deque.appendleft(0)
print(my_deque) # Output: deque([0, 1, 2, 3, 4])

# Remove from the right
my_deque.pop()
print(my_deque) # Output: deque([0, 1, 2, 3])

# Remove from the left
my_deque.popleft()
print(my_deque) # Output: deque([1, 2, 3])