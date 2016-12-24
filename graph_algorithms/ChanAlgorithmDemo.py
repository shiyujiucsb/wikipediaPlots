'''
Convex Hull Demo (SVG) for Chan's algorithm.
Firstly use this code to generate SVG frames.
Then transform to bitmaps and convert to GIF.
'''

# range size
N, M = 300, 900
margin = 20

def saveToSVG(nFrames, points, partitions, firmed, trying):
    f = open('demo_'+'0'*(3-len(str(nFrames)))+str(nFrames)+'.svg', 'w')
    f.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\n")
    for p in points:
        f.write("<circle cx=\"" +str(p[0]+margin)+ "\" cy=\""+ str(N-p[1]+margin) +"\" r=\"5\" fill=\"white\" stroke=\"black\"/>\n")
    for par in partitions:
        for i in range(len(par)-1):
            f.write("<line x1=\"" +str(par[i][0]+margin)+ "\" y1=\""+ str(N-par[i][1]+margin) +"\" x2=\"" + str(par[i+1][0]+margin) + "\" y2=\"" + str(N-par[i+1][1]+margin) + "\" stroke=\"grey\" stroke-width=\"3\"/>\n")
        f.write("<line x1=\"" +str(par[-1][0]+margin)+ "\" y1=\""+ str(N-par[-1][1]+margin) +"\" x2=\"" + str(par[0][0]+margin) + "\" y2=\"" + str(N-par[0][1]+margin) + "\" stroke=\"grey\" stroke-width=\"3\"/>\n")
    for i in range(len(firmed)-1):
        f.write("<line x1=\"" +str(firmed[i][0]+margin)+ "\" y1=\""+ str(N-firmed[i][1]+margin) +"\" x2=\"" + str(firmed[i+1][0]+margin) + "\" y2=\"" + str(N-firmed[i+1][1]+margin) + "\" stroke=\"red\" stroke-width=\"5\"/>\n")
    for i in range(len(trying)-1):
        f.write("<line x1=\"" +str(trying[i][0]+margin)+ "\" y1=\""+ str(N-trying[i][1]+margin) +"\" x2=\"" + str(trying[i+1][0]+margin) + "\" y2=\"" + str(N-trying[i+1][1]+margin) + "\" stroke=\"blue\" stroke-width=\"5\"/>\n")
    f.write("</svg>\n")
    f.close()

def generatePoints(n):
    import random as r
    r.seed(100)
    
    res = []
    for i in range(n):
        pt = [r.randint(0,M), r.randint(0,N)]
        if [pt] not in res:
            res += [pt]
    return res

def norm(x, y):
    return (x*x+y*y)**.5

def dotProductNormed(x1, y1, x2, y2):
    return (x1*x2+y1*y2)/norm(x1, y1)/norm(x2, y2)

def cross(x1, y1, x2, y2):
    return x1*y2 - x2*y1

def graham(n, points):
    if n<3: return
    points.sort(key = lambda x: x[1])
    first = points[0]
    rest = points[1:]
    rest.sort(key = lambda x: -dotProductNormed(x[0]-points[0][0], x[1]-points[0][1], 1, 0))
    points = [first] + rest
    stack = [points[0], points[1]]
    i=2
    while i<n:
        x0, y0 = stack[-2][0], stack[-2][1]
        x1, y1 = stack[-1][0], stack[-1][1]
        x2, y2 = points[i][0], points[i][1]
        if cross(x1-x0, y1-y0, x2-x0, y2-y0)<0:
            stack.pop()
        else:
            stack += [points[i]]
            i+=1
    return stack

# TODO: may be improved.
def tangentPoint(t, hull):
    n = len(hull)
    if t in hull:
        for i in range(len(hull)):
            if hull[i] == t:
                return hull[(i+1)%n]
    if cross(hull[0][0]-t[0], hull[0][1]-t[1], hull[-1][0]-t[0], hull[-1][1]-t[1])>=0 and cross(hull[1][0]-t[0], hull[1][1]-t[1], hull[0][0]-t[0], hull[0][1]-t[1])<=0:
        return hull[0]
    if cross(hull[0][0]-t[0], hull[0][1]-t[1], hull[-1][0]-t[0], hull[-1][1]-t[1])<=0 and cross(hull[-1][0]-t[0], hull[-1][1]-t[1], hull[-2][0]-t[0], hull[-2][1]-t[1])>=0:
        return hull[-1]
    low, high = 1, n-2
    while low+1<high:
        i = low + (high-low)//2
        if cross(hull[i][0]-t[0], hull[i][1]-t[1], hull[i-1][0]-t[0], hull[i-1][1]-t[1])>=0 and cross(hull[i+1][0]-t[0], hull[i+1][1]-t[1], hull[i][0]-t[0], hull[i][1]-t[1])<=0:
            return hull[i]
        if cross(hull[i][0]-t[0], hull[i][1]-t[1], hull[i-1][0]-t[0], hull[i-1][1]-t[1])>=0 and cross(hull[i+1][0]-t[0], hull[i+1][1]-t[1], hull[i][0]-t[0], hull[i][1]-t[1])>=0:
            if cross(hull[i][0]-t[0], hull[i][1]-t[1], hull[low][0]-t[0], hull[low][1]-t[1])<=0:
                if cross(hull[high+1][0]-t[0], hull[high+1][1]-t[1], hull[high][0]-t[0], hull[high][1]-t[1])>=0 and cross(hull[high][0]-t[0], hull[high][1]-t[1], hull[high-1][0]-t[0], hull[high-1][1]-t[1])>=0:
                    high = i
                else: low = i
            else: low = i
        else:
            if cross(hull[i][0]-t[0], hull[i][1]-t[1], hull[low][0]-t[0], hull[low][1]-t[1])>=0:
                if cross(hull[low+1][0]-t[0], hull[low+1][1]-t[1], hull[low][0]-t[0], hull[low][1]-t[1])<=0 and cross(hull[low][0]-t[0], hull[low][1]-t[1], hull[low-1][0]-t[0], hull[low-1][1]-t[1])<=0:
                    low = i
                else: high = i
            else: high = i
    for i in range(n):
        j = (low+i)%n
        if cross(hull[j][0]-t[0], hull[j][1]-t[1], hull[j-1][0]-t[0], hull[j-1][1]-t[1])>=0 and cross(hull[j+1][0]-t[0], hull[j+1][1]-t[1], hull[j][0]-t[0], hull[j][1]-t[1])<=0:
            return hull[j]

def javis(s, hulls):
    n = len(hulls)
    t = s
    res = [s]
    nframe = 1
    while True:
        next_pt = t
        for hull in hulls:
            p = tangentPoint(t, hull)
            saveToSVG(nframe, pts, hulls, res, [res[-1], p])
            nframe+=1
            if next_pt == t or cross(p[0]-t[0], p[1]-t[1], next_pt[0]-t[0], next_pt[1]-t[1])>0 :
                next_pt = p
        if next_pt == s:
            res += [s]
            break
        else:
            t = next_pt
            res += [next_pt]
            saveToSVG(nframe, pts, hulls, res, [])
            nframe+=1
    saveToSVG(nframe, pts, hulls, res, [])
    return res

# test 120 points temporarily
n = 120
pts = generatePoints(n)
pts.sort(key = lambda x: x[0])
nPartition = 4
hulls = []
for i in range(nPartition):
    hulls.append(graham(n//nPartition, pts[i*n//nPartition:(i+1)*n//nPartition]))
saveToSVG(0, pts, hulls, [], [])
start = hulls[0][0]
for hull in hulls:
    for pt in hull:
        if pt[1]<start[1] or (pt[1]==start[1] and pt[0] < start[0]):
            start = pt
javis(start, hulls)
