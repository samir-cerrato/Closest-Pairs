import math
import sys

def euclidean_distance_squared(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def closest_pair_preprocessing(P):
    Px = sorted(enumerate(P), key=lambda p: p[1][0])
    Py = sorted(enumerate(P), key=lambda p: p[1][1])
    return Px, Py

def closest_pair_recursive(Px, Py):
    n = len(Px)
    
    if n <= 3:
        return min(euclidean_distance_squared(Px[i][1], Px[j][1]) for i in range(n) for j in range(i+1, n))
    
    Line = n // 2
    Left_x = Px[:Line]
    Right_x = Px[Line:]
    Left_y = []
    Right_y = []
    
    for p in Py:
        if p[0] < Left_x[-1][0]:
            Left_y.append(p)
        else:
            Right_y.append(p)
    
    closest_left = closest_pair_recursive(Left_x, Left_y)
    closest_right = closest_pair_recursive(Right_x, Right_y)
    delta = min(closest_left, closest_right)
    
    middle_x = Left_x[-1][1][0]
    strip = [p for p in Py if middle_x - delta <= p[1][0] <= middle_x + delta]
    
    strip_length = len(strip)
    strip.sort(key=lambda p: p[1][1])  # Sort by y-coordinate
    
    for i in range(strip_length):
        for j in range(i+1, min(i+8, strip_length)):
            delta = min(delta, euclidean_distance_squared(strip[i][1], strip[j][1]))
    
    return delta

def main():
    lines = sys.stdin.readlines()
    P = [tuple(map(int, line.strip().split())) for line in lines]
    
    Px, Py = closest_pair_preprocessing(P)
    closest_distance = closest_pair_recursive(Px, Py)
    
    print(closest_distance)

if __name__ == "__main__":
    main()