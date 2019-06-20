def find_flight(n, flights, src, dst, k):
    """
    https://leetcode.com/problems/cheapest-flights-within-k-stops/

    @params n (int): number of cities (nodes)
    @params flights (list[list]) [[0,1,100],[1,2,100],[0,2,500]]
      denote edge (src, dst, price)
    @params src (int): start node index
    @params dst (int): destination node index
    @params k (int): at most k stops (direct flight is 0 stop)

    @return (int) cheapest price, -1 if no such flight to dst within K stops
    """
    
