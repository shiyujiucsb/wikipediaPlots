'''
Minimum Spanning Tree generation (SVG) for Kruskal's algorithm.
Firstly use this code to generate SVG frames.
Then transform to bitmaps and convert to GIF.
'''

# range size
N = 300
margin = 20

def norm(x, y):
    return (x*x+y*y)**.5

class Edge(object):
    def __init__(self, source, target, points):
        self.u = source
        self.v = target
        self.len = norm(points[source][0]-points[target][0], points[source][1]-points[target][1])

class UnionNode(object):
    def __init__(self):
        self.next = None

def saveToSVG(nFrames, points, firmed, trying):
    f = open('demo_'+'0'*(3-len(str(nFrames)))+str(nFrames)+'.svg', 'w')
    f.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\n")
    for p in points:
        f.write("<circle cx=\"" +str(p[0]+margin)+ "\" cy=\""+ str(N-p[1]+margin) +"\" r=\"5\" fill=\"white\" stroke=\"black\"/>\n")
    for L in firmed:
        f.write("<line x1=\"" +str(L[0][0]+margin)+ "\" y1=\""+ str(N-L[0][1]+margin) +"\" x2=\"" + str(L[1][0]+margin) + "\" y2=\"" + str(N-L[1][1]+margin) + "\" stroke=\"red\" stroke-width=\"5\"/>\n")
    for L in trying:
        f.write("<line x1=\"" +str(L[0][0]+margin)+ "\" y1=\""+ str(N-L[0][1]+margin) +"\" x2=\"" + str(L[1][0]+margin) + "\" y2=\"" + str(N-L[1][1]+margin) + "\" stroke=\"blue\" stroke-width=\"5\"/>\n")
    f.write("</svg>\n")
    f.close()

def generatePoints(n):
    import random as r
    r.seed(100)
    
    res = []
    for i in range(n):
        pt = [r.randint(0,N) for _ in [0, 1]]
        if [pt] not in res:
            res += [pt]
    return res

def kruskal(n, points):
    n = len(points)
    union = [UnionNode() for _ in points]
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            e = Edge(i, j, points)
            edges.append(e)
    edges.sort(key = lambda x:-x.len)
    mst = []
    nframe = 0
    saveToSVG(nframe, points, mst, [])
    nframe+=1
    while len(mst)<n-1:
        s = edges[-1].u
        t = edges[-1].v
        saveToSVG(nframe, points, mst, [[points[s], points[t]]])
        nframe+=1
        p = union[s]
        q = union[t]
        while p.next != None: p = p.next
        while q.next != None: q = q.next
        if p!=q:
            newNode = UnionNode()
            p.next = q.next = newNode
            mst.append([points[s], points[t]])
            saveToSVG(nframe, points, mst, [])
            nframe+=1
        edges.pop()
    return mst

# test 30 points temporarily
n = 30
pts = generatePoints(n)
kruskal(n, pts)
