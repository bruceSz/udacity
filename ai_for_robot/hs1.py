
def main():
    print "Entry."

world = ['red','green','green','red','red','red']
# note the meaning of pHits and pMiss. probability of reside some place
# where  when acclaim sth and measured sth.
# and probability of reside some place where acclaim sth and measured not .

pHit = 0.6
pMiss = 0.2

pExact=0.8
pOver=0.1
pUnder=0.1

def sense(p,Z):
    q = []
    for i in range(len(p)):
        hit  == (Z == world[i])
        q.append(p[i]*(pHit*hit + pMiss(1-hit)))
    s = sum(q)
    q = [i/s for i in q]
    return q




def move(p,U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)]
        s = s+pOver * p[(i-U-1)%len(p)]
        s = s + pUnder * p[(i-U+1) %len(p)]
        q.append(s)

    return q

world2D = [['green','red','green'],
           ['green','red','red'],
           ['green','green','green']]

measurements2D = ['red']
motions2D = [[0,0],[0,1]]

def sense2D(p, Z):
    q  = []
    for i in range(len(p)):
        for j in range(len(p[0])):
            hit  = (Z == p[i][j])
            q.append(p[i][j]*(pHit*(hit)+pMiss(1-hit)))
    tmp_s = 0.0

    return  q


def move2D(p,U):
    for i in range(len())



if __name__ == "__main__":
    main()