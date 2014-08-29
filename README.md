A collection of data structure and algorithms implementation based on Python 2.7.3

LinkedList -- A singly linked list inheriting `collections.MutableSequence` to provide indexed based operations
Some test to show time cost of accessing or changing elements in linked list compared to built-in list

```sh
python -m timeit -s 'l=[i for i in range(100000)]' l[0]
10000000 loops, best of 3: 0.0525 usec per loop

python -m timeit -s 'l=[i for i in range(100000)]' l[1000]
10000000 loops, best of 3: 0.052 usec per loop

python -m timeit -s 'l=[i for i in range(100000)]' l[50000]
10000000 loops, best of 3: 0.052 usec per loop

python -m timeit -s 'from linkedlist import *; iter=[i for i in range(100000)]; ll=LinkedList(iter)' ll[0]
1000000 loops, best of 3: 0.952 usec per loop

python -m timeit -s 'from linkedlist import *; iter=[i for i in range(100000)]; ll=LinkedList(iter)' ll[1000]
10000 loops, best of 3: 126 usec per loop

python -m timeit -s 'from linkedlist import *; iter=[i for i in range(100000)]; ll=LinkedList(iter)' ll[50000]
100 loops, best of 3: 7.62 msec per loop
```

We can see that time cost of accessing an element in linked list is proportionate to the position where it sits. More time needed as it moves towards the back while array-based list remains constant.
