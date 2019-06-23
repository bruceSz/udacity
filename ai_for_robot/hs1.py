
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
p_move = 0.5


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'


def localize(colors, measurements, motions, sensor_right, p_move):
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    print "Before move."
    show(p)


    def sense2D(p, Z):
        q  = []
        for i in range(len(p)):
            tmp = []
            for j in range(len(p[0])):
                hit = (Z == colors[i][j])
                if hit:
                    print "hit at", i,j
                tmp.append(p[i][j]*(sensor_right*(hit)+(1-sensor_right)*(1-hit)))
            q.append(tmp)
        tmp_s = 0.0

        for i in range(len(p)):
            for j in range(len(p[0])):
                tmp_s += q[i][j]

        print "sense normal denominator.", tmp_s
        for i in range(len(q)):
            for j in range(len(q[0])):
                q[i][j] = q[i][j]/tmp_s

        return  q


    def move2D(p,U):
        if len(p) == 0:
            return
        col_b = 0
        col_e = len(p[0])
        row_b = 0
        row_e = len(p)

        q = []
        # do init.
        for i in range(len(p)):
            tmp = []
            for j in range(len(p[0])):
                tmp.append(0.0)
            q.append(tmp)

        for i in range(len(p)):
            for j in range(len(p[0])):
                row, col = U[0], U[1]
                from_r = (i - row)%row_e
                from_c = (j - col)%col_e
                if (from_r >=row_b and from_r < row_e) and (from_c >=col_b and from_c < col_e ):
                    q[i][j] = p_move * p[from_r][from_c] #+ (1-p_move)*p[i][j]
                    print "idx:", i, j , "from ", from_r, from_c, " with prob", q[i][j]
                else:
                    print "can not move from ", from_r, from_c,"inx of curr: ", i,j, "with row ", row_b, row_e, " col: ", col_b, col_e
        tmp_s = 0.0

        #for i in range(len(p)):
        #    for j in range(len(p[0])):
        #        tmp_s += q[i][j]

        #print "sense normal denominator.", tmp_s
        #for i in range(len(q)):
        #    for j in range(len(q[0])):
        #        q[i][j] = q[i][j] / tmp_s

        return q

    for i in range(len(measurements)):
        p = sense2D(p,measurements[i])
        print "after sense with measure ",i ,measurements[i]
        show(p)
        p = move2D(p,motions[i])
        print "after move ", i, motions[i]
        show(p)

    print "after all."
    show(p)


def test1():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'G'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0]])


def test2():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.5, 0.5],
         [0.0, 0.0, 0.0]])

def test3():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.06666666666, 0.06666666666, 0.06666666666],
         [0.06666666666, 0.26666666666, 0.26666666666],
         [0.06666666666, 0.06666666666, 0.06666666666]])


def test4():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.03333333333, 0.03333333333, 0.03333333333],
         [0.13333333333, 0.13333333333, 0.53333333333],
         [0.03333333333, 0.03333333333, 0.03333333333]])

def test5():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.0, 1.0],
         [0.0, 0.0, 0.0]])


def test6():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 0.8
    p_move = 0.5
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.0289855072, 0.0289855072, 0.0289855072],
         [0.0724637681, 0.2898550724, 0.4637681159],
         [0.0289855072, 0.0289855072, 0.0289855072]])


def test7():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 1.0
    p_move = 0.5
    p = localize(colors, measurements, motions, sensor_right, p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.33333333, 0.66666666],
         [0.0, 0.0, 0.0]])


def main():
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    #test6()
    test7()



if __name__ == "__main__":
    main()