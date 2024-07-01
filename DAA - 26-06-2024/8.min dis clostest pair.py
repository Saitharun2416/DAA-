import math

def d(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def c(a):
    m= float('inf')
    c= None

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            dis= d(a[i], a[j])
            if dis< m:
                m= dis
                c= (a[i], a[j])
    
    return c, m

a = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pair, dist = c(a)
print("The clostest pair of points is ",pair," with a distance of ",round(dist,4))
