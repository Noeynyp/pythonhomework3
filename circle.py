import turtle

def draw_circle(radius):
    colors = ["blue", "black", "red", "yellow", "green"]
    positions = [(-2 * radius, 0), (0, 0), (2 * radius, 0), (-radius, -radius), (radius, -radius)]
    
    screen = turtle.Screen()
    screen.bgcolor("white")
 
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(5)
    
    for i in range(5):
        pen.penup()
        x, y = positions[i]
        pen.goto(x, y - radius)
        pen.pendown()
        pen.color(colors[i])
        pen.circle(radius)
    
    pen.hideturtle()
    screen.mainloop()

def main():
    try:
        radius = float(input("Enter the radius of the ring: "))
        draw_circle(radius)
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()
