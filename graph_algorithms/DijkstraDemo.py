'''
Dijkstra's shortest path covering (SVG) using priority queue.
Firstly use this code to generate SVG frames.
Then transform to bitmaps and convert to GIF.
'''

# range size
N = 300
margin = 20

def norm(px, py):
    return ((px[0]-py[0])**2+(px[1]-py[1])**2)**.5

def saveToSVG(nFrames, points, edges, firmed, relaxing):
    f = open('demo_'+'0'*(3-len(str(nFrames)))+str(nFrames)+'.svg', 'w')
    f.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\n")
    for p in points:
        f.write("<circle cx=\"" +str(p[0]+margin)+ "\" cy=\""+ str(N-p[1]+margin) +"\" r=\"5\" fill=\"white\" stroke=\"black\"/>\n")
    for i in range(len(edges)):
        for j in edges[i]:
            f.write("<line x1=\"" +str(points[i][0]+margin)+ "\" y1=\""+ str(N-points[i][1]+margin) +"\" x2=\"" + str(points[j][0]+margin) + "\" y2=\"" + str(N-points[j][1]+margin) + "\" stroke=\"grey\" stroke-width=\".5\"/>\n")
    for L in firmed:
        f.write("<line x1=\"" +str(L[0][0]+margin)+ "\" y1=\""+ str(N-L[0][1]+margin) +"\" x2=\"" + str(L[1][0]+margin) + "\" y2=\"" + str(N-L[1][1]+margin) + "\" stroke=\"red\" stroke-width=\"5\"/>\n")
    for L in relaxing:
        f.write("<line x1=\"" +str(L[0][0]+margin)+ "\" y1=\""+ str(N-L[0][1]+margin) +"\" x2=\"" + str(L[1][0]+margin) + "\" y2=\"" + str(N-L[1][1]+margin) + "\" stroke=\"blue\" stroke-width=\"5\"/>\n")
    f.write("</svg>\n")
    f.close()

def generatePoints(n):
    import random as r
    r.seed(10)
    
    res = []
    for i in range(n):
        pt = [r.randint(0,N) for _ in [0, 1]]
        if [pt] not in res:
            res += [pt]
    return res

def generateEdges(n, points):
    import random as r
    r.seed(10)
    edges = []
    for i in range(n):
        dst = []
        for j in range(n):
            if i!=j and norm(points[i], points[j]) < N/3:
                dst.append(j);
        edges.append(dst)
    return edges

def dijkstra(n, points, edges):
    nframe = 0
    dist = [float("inf") for i in range(n)]
    prev = [-1 for _ in range(n)]
    cover = []
    import heapq
    dist[0] = 0.0
    heap = [[dist[i], i] for i in range(n)]
    while len(heap)>0:
        u = heap[0][1]
        if prev[u]!=-1:
            cover.append([points[prev[u]], points[u]])
        saveToSVG(nframe, points, edges, cover, [])
        nframe+=1
        heapq.heappop(heap)
        for i in edges[u]:
            if i!=u and dist[i] > dist[u] + norm(points[i], points[u]):
                dist[i] = dist[u] + norm(points[i], points[u])
                prev[i] = u
                for j in range(len(heap)):
                    if heap[j][1] == i:
                        heap[j][0] = dist[i]
                        break
                heapq.heapify(heap)
                saveToSVG(nframe, points, edges, cover, [[points[u], points[i]]])
                nframe+=1
    
    return dist, prev

# test 30 points temporarily
n = 30
pts = generatePoints(n)
es = generateEdges(n, pts)
dijkstra(n, pts, es)
