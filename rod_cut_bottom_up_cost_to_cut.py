from numpy import zeros

def rod_cut(n, p, c):
    bestprices = zeros(n+1, dtype=int)
    nextcuts = zeros(n+1, dtype=int)
    bestprices[0] = 0
    nextcuts[0] = 0
    bestprices[1] = p[0]
    nextcuts[1] = 1
    for i in range(2, n+1): # i from 2 to n
        for nextcut in range(1, i+1): # from 1 to i
            if nextcut<i: # i.e. if we actually make a cut
                cost = c
            else:
                cost = 0
            if bestprices[i-nextcut]+p[nextcut-1]-cost>bestprices[i]:
                bestprices[i] = bestprices[i-nextcut]+p[nextcut-1]-cost
                nextcuts[i] = nextcut
    # reconstruct solution
    bestcuts = []
    bestprice = bestprices[n]
    while n:
        bestcuts.append(nextcuts[n])
        n -= nextcuts[n]
    return bestprice, bestcuts

# no cost: get the old solution
print rod_cut(8, [1, 5, 8, 9, 10, 17, 17, 20], 0)

# high cost: always avoid cutting
print rod_cut(8, [1, 5, 8, 9, 10, 17, 17, 20], 1000)

# crossover: get the old solution
for cost in range(5):
    print "Cost", cost, "solution", rod_cut(8, [1, 5, 8, 9, 10, 17, 17, 20], cost)