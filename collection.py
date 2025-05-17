# collections: Counter,namedtuple,orderedDict,
from collections import Counter
a = "aaaaaaaacccccccbbbb"
count = Counter(a)
print(count)    # gives dictionary
print(count.items())  #results dictionary
print(count.keys())
print(count.values())
print(count.most_common(1))  # most common element with lists inside tuples
print(count.most_common(1)[0][0])
print(list(count.elements()))
