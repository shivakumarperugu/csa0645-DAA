import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

chars = ['a','b','c','d']
freq = [5,9,12,13]

heap = []

for c, f in zip(chars, freq):
    heapq.heappush(heap, Node(f, c))

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, Node(a.freq+b.freq, left=a, right=b))

root = heap[0]

encoded = "1101100111110"

ans = ""
curr = root

for bit in encoded:
    if bit == '0':
        curr = curr.left
    else:
        curr = curr.right

    if curr.char:
        ans += curr.char
        curr = root

print(ans)