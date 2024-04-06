import math

def area_of_polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

if __name__ == "__main__":
    n = int(input("Enter the number of sides of the polygon: "))
    s = float(input("Enter the length of each side of the polygon: "))

    area = area_of_polygon(n, s)

    print("Area of the", n, "-sided polygon:", area)
    
