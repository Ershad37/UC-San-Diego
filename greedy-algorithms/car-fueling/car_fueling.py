from sys import stdin

def min_fueling(d, m, stops):
    if d < m: return 0
    route = [0] + stops + [d]
    refilled = 0
    current_stop = 0
    n = len(route)

    while current_stop < n - 1:
        last_stop = current_stop

        while current_stop < n - 1 and route[current_stop + 1] - route[last_stop] <= m:
            current_stop += 1
        
        if current_stop == last_stop:
            return -1
        
        if current_stop < n - 1:
            refilled += 1

    return refilled

                
if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_fueling(d, m, stops))









