"""

"When you know the space" -> Arrays -> Constant access (You know...)
"When you want the latest item inserted" -> Stacks -> LIFO (Recursion)
"When you want to replicate a normal line" -> Queues -> FIFO (Ride Line)
"When you want to have fast operations at the beginning or end of line" -> Linked List
    * Blockchain (Each block mentions the previous one)
"When you need to search faster" -> Trees -> We will get to

"You want the max or min of a list" -> Heaps
O(log(n)) insert
O(1) removal

   1,2,3,4,5,6,7,8,9,10,11 -> (i = index of the value in the array)
[-,T,S,R,P,N,O,A,E,I,H,G]
Left = 2i
Right = 2i + 1
            T
       S          R
    P      N     O A
  E  I    H G

-- Min Heap --
        3
    4       9
  5   7

-- Balanced Binary Search Tree --
        7
    5       9
  3   4

  -- Array Way --
  [5,7,9,4,3]
  Lowest Element -> O(N)
  Add Next Element -> O(1)

  -- Heap Way --
  [3,4,9,5,7]
  Lowest Element -> O(1)
  Add Next Element -> O(log(N))

    For 1 Million items:
        Array -> 1 Million Operations
        Heap -> 20 Operations
    PER INSERT OR REMOVAL

    If I added 1 million elements 1 by 1 to a list and for each time

    --- All Values Are Removed From Left Side Of Array ---
    Min Heap, get 2nd Max Value
    [1,2,3,4] --> Remove lowest value (check length of Heap) continue until length = 2 return 0 index then

    Max Heap, get 2nd Min Value
    [5,4,2,1] --> Remove largest value (check length of Heap) continue until length = 2 return 0 index then

    PriorityQueue<Integer> heap = new PriorityQueue<>(); // Min Heap
    PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder()); // Max Heap

    .poll() -> Removes element on top (O(log(n))
    .peek() -> Returns value on top, but doesnt remove (O(1))
    .add() -> Adds into heap (O(log(n))

    while (heap.size() > 2) {
        heap.poll();
    }

    return heap.peek();

"""
import heapq

heap = [5, 7, 9, 4, 3]

heapq.heapify(heap)

if __name__ == "__main__":
    print(heap)
