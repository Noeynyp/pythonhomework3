import turtle

def draw_star(length):

    star_turtle = turtle.Turtle()
    star_turtle.speed(1)

    for _ in range(5):
        star_turtle.forward(length)
        star_turtle.right(144)

    turtle.done()

def main():
    try:
        length = float(input("Enter the length of the star: "))
        draw_star(length)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
