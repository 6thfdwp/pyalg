A collection of data structure and algorithms implementation based on Python 2.7.3

##LinkedList -- A singly linked list 

Inherit `collections.MutableSequence` to provide indexed based operations


- Compare time cost of accessing element in linked list with that of built-in list

```sh
python -m timeit -s 'l=[i for i in range(100000)]' l[0]
10000000 loops, best of 3: 0.0525 usec per loop

python -m timeit -s 'l=[i for i in range(100000)]' l[1000]
10000000 loops, best of 3: 0.052 usec per loop

python -m timeit -s 'l=[i for i in range(100000)]' l[50000]
10000000 loops, best of 3: 0.052 usec per loop

python -m timeit -s 'from linkedlist import *; iter=range(100000); ll=LinkedList(iter)' ll[0]
1000000 loops, best of 3: 0.952 usec per loop

python -m timeit -s 'from linkedlist import *; iter=range(100000); ll=LinkedList(iter)' ll[1000]
10000 loops, best of 3: 126 usec per loop

python -m timeit -s 'from linkedlist import *; iter=range(100000); ll=LinkedList(iter)' ll[50000]
100 loops, best of 3: 7.62 msec per loop
```
We can see that time cost of accessing an element in linked list is proportionate to the position where it sits. More time needed as it moves towards the back while array-based list remains constant. See [Official design faq for list implementation](https://docs.python.org/2/faq/design.html#how-are-lists-implemented)


- Compare time cost of insert element in the front of linked list with that of built-in list
```sh
# only run 10 loops for insertion
python -m timeit -s 'from linkedlist import *; iter=range(100000); ll=LinkedList(iter)' -n 10 'll.insert(0,9)'
10 loops, best of 3: 2.19 usec per loop

python -m timeit -s 'from linkedlist import *; iter=range(1000000); ll=LinkedList(iter)' -n 10 'll.insert(0,9)'
10 loops, best of 3: 2.19 usec per loop

python -m timeit -s 'l=range(100000)' -n 10 'l.insert(0,9)'
10 loops, best of 3: 96.9 usec per loop

python -m timeit -s 'l=range(1000000)' -n 10 'l.insert(0,9)'
10 loops, best of 3: 3.71 msec per loop
```
We can see linked list is suitable for frequent insertion task, it stays constant regardless of the length while array-based list is much more time consuming since it involves moving a lot of elements to make new room.


## *Others to be continued*
