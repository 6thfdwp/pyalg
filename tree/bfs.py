from collections import deque, defaultdict
import heapq

def find_flight(flights, src, dst, k):
    """
    https://leetcode.com/problems/cheapest-flights-within-k-stops/

    @params n (int): number of cities (nodes)
    @params flights (list[list]) [[0,1,100],[1,2,100],[0,2,500]]
      denote edge (src, dst, price)
    @params src (int): start node index
    @params dst (int): destination node index
    @params k (int): at most k stops (direct flight is 0 stop, the adjacent cities)

    @return (int) cheapest price, -1 if no such flight to dst within K stops
    Consider it is a directed graph without duplicate flight between two or self cycles
    """
    G = defaultdict(list)
    def build(flights):
      for flight in flights:
        s, to, price = flight
        G[s].append((to, price))

    build(flights)
    print G
    # (cost, idx, stops)
    # we need to consider cost and stops (the bfs depth)
    # init with -1 as src adjcency considered direct without stop (stop = 0)
    PQ = [(0, src, -1)]
    res = None
    while PQ:
        # extract node with lowest cost so far
        cost, s, stops = heapq.heappop(PQ)
        print cost, s, stops
        # when dst is popped and check how many steps from src to dst 
        # if <=k stop processing queue, otherwise continue to find higher cost
        # but explored before (closer to src)
        if s == dst and stops <= k:
            res = (cost, s, stops)
            break
        for dest in G[s]:
            to, price = dest
            # always add to PQ as cheaper flights might have more stops
            heapq.heappush(PQ, (cost+price, to, stops+1))

    print res

def explore_maze(maze, start, end):
    """
    @params maze (list[list]):
        [ [1,1,1,1,1], ['S',1,'X',1,1], [1,1,1,1,1], ['X',1,1,'E',1], [1,1,1,1,'X'] ]
            1 1 1 1 1
            S 1 X 1 1
            1 1 1 1 1
            X 1 1 E 1
            1 1 1 1 X
    @params start (tuple): [1,0]
    @params start (tuple): [3,3]

    can either traverse up, down, left or right except X
    @return (list[tuple]): [(3, 2), (3, 1), (2, 1), (2, 0)] one possible path
    """
    rows, cols = len(maze)-1, len(maze[0])-1
    def edges(cell):
        # cell, depth = node
        r, c = cell
        e = []
        if r - 1 >= 0 and maze[r-1][c] == 1:
            e.append((r-1, c))
        if c - 1 >= 0 and maze[r][c-1] == 1: # left
            e.append((r, c-1))
        if r + 1 <= rows and maze[r+1][c] != 'X': # down
            e.append((r+1, c))
        if c + 1 <= cols and maze[r][c+1] != 'X': # right
            e.append((r, c+1))
        # print e
        return e

    def genpath(paths, node):
        if node == start:
            return []

        p = paths[node][0]
        if p == start:
            return genpath(paths, p)
        else:
            return genpath(paths, p) + [p]

    Q = deque([start])
    # (r, c) tuple is hashable, the equality is based on value of r and c
    # no matter we create a new tuple for every cell state, they are equal as long as r,c is the same
    visited = set()
    paths = {} # {cell: [parent, depth]}
    while Q:
        v = Q.popleft()
        visited.add(v)
        print 'visited node: %s' % str(v)
        if v == end:
            break
        for cell in edges(v):
            # do not put visited state again
            # also it is unweighted, if the state is put in the Q (visiting) to be explored later
            # no need to put in the Q as well or update the paths
            if cell in visited or cell in paths:
                continue
            print cell
            paths[cell] = [v] # record parent of current visiting
            Q.append(cell)

    if end in paths:
        return genpath(paths, end)

    return None


if __name__ == '__main__':
    maze = [ [1,1,1,1,1], [1,1,'X',1,1], [1,1,1,1,1], ['X',1,1,1,1], [1,'X',1,1,'X'] ]
    # start, end = (4,3), (1,0),  #(3,3)
    # print explore_maze(maze, start, end)
    flights = [[0,1,100],[1,2,100],[1,3,10],[3,0,10],[3,2,50],[0,2,500]]
    flights = [[]]
    flights = [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
    # find_flight(flights, 0, 2, 0)
    find_flight(flights, 1, 4, 5)
