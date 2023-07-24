def tri_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    
    area = 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

    return area

def main():
    try:
        # Input the three points
        x1, y1 = map(float, input("Enter the coordinates of point p1: ").split(','))
        x2, y2 = map(float, input("Enter the coordinates of point p2: ").split(','))
        x3, y3 = map(float, input("Enter the coordinates of point p3: ").split(','))

        area = tri_area((x1, y1), (x2, y2), (x3, y3))

        
        print("Area of the triangle:", area)
    except ValueError:
        print("Invalid input. Please enter the coordinates as floating-point numbers separated by a comma.")

if __name__ == "__main__":
    main()
